from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ecommerce.apps.payments.models import Payment
from ecommerce.apps.orders.models import Order
from ecommerce.apps.payments.serializers import PaymentSerializer, PaymentProcessSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(order__user=self.request.user)

    @action(detail=False, methods=['post'])
    def process_payment(self, request):
        serializer = PaymentProcessSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(id=serializer.validated_data['order_id'], user=request.user)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        if order.status != 'pending':
            return Response({'error': 'Order cannot be paid'}, status=status.HTTP_400_BAD_REQUEST)

        payment, created = Payment.objects.get_or_create(
            order=order,
            defaults={
                'amount': order.total,
                'payment_method': serializer.validated_data['payment_method'],
                'status': 'pending'
            }
        )

        # Simulate payment processing
        payment.status = 'completed'
        payment.transaction_id = f"TXN-{order.order_number}-12345"
        payment.save()

        order.status = 'paid'
        order.save()

        return Response({
            'message': 'Payment processed successfully',
            'payment': PaymentSerializer(payment).data
        }, status=status.HTTP_200_OK)
