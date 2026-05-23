from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
from uuid import uuid4

from ecommerce.apps.orders.models import Order, OrderItem
from ecommerce.apps.cart.models import Cart
from ecommerce.apps.promotions.models import Coupon
from ecommerce.apps.orders.serializers import OrderSerializer, OrderCreateSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def create_order(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart = Cart.objects.get(user=request.user)
            if not cart.items.exists():
                return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

            subtotal = cart.total_price
            shipping_cost = serializer.validated_data['shipping_cost']
            tax = serializer.validated_data['tax']
            discount = serializer.validated_data.get('discount', 0)
            
            coupon_code = serializer.validated_data.get('coupon_code')
            if coupon_code:
                try:
                    coupon = Coupon.objects.get(code=coupon_code)
                    if coupon.is_valid() and subtotal >= coupon.min_order_amount:
                        if coupon.discount_type == 'percentage':
                            discount = (subtotal * coupon.discount_value) / 100
                        else:
                            discount = coupon.discount_value
                except Coupon.DoesNotExist:
                    pass

            total = subtotal + shipping_cost + tax - discount

            order = Order.objects.create(
                user=request.user,
                order_number=f"ORD-{uuid4().hex[:8].upper()}",
                subtotal=subtotal,
                shipping_cost=shipping_cost,
                tax=tax,
                discount=discount,
                total=total,
                shipping_address=serializer.validated_data['shipping_address'],
                billing_address=serializer.validated_data.get('billing_address', serializer.validated_data['shipping_address']),
                status='pending'
            )

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.price_at_purchase
                )

            cart.items.all().delete()

            return Response({
                'message': 'Order created successfully',
                'order': OrderSerializer(order).data
            }, status=status.HTTP_201_CREATED)

        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        order = self.get_object()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
