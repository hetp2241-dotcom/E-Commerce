from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ecommerce.apps.checkout.serializers import CheckoutSerializer
from ecommerce.apps.cart.models import Cart
from ecommerce.apps.shipping.models import ShippingMethod

class CheckoutViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def validate(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart = Cart.objects.get(user=request.user)
            if not cart.items.exists():
                return Response({'valid': False, 'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

            shipping_method = ShippingMethod.objects.get(id=serializer.validated_data['shipping_method'])

            return Response({
                'valid': True,
                'summary': {
                    'subtotal': cart.total_price,
                    'shipping': shipping_method.cost,
                    'tax': 0,
                    'total': cart.total_price + shipping_method.cost
                }
            })
        except Cart.DoesNotExist:
            return Response({'valid': False, 'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        except ShippingMethod.DoesNotExist:
            return Response({'valid': False, 'error': 'Shipping method not found'}, status=status.HTTP_404_NOT_FOUND)
