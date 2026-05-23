from rest_framework import serializers
from ecommerce.apps.payments.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'status', 'payment_method', 'transaction_id', 'created_at']

class PaymentProcessSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    payment_method = serializers.CharField()
    token = serializers.CharField(required=False, allow_blank=True)
