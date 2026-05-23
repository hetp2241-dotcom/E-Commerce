from rest_framework import serializers

class CheckoutSerializer(serializers.Serializer):
    shipping_address = serializers.CharField()
    billing_address = serializers.CharField(required=False)
    shipping_method = serializers.IntegerField()
    coupon_code = serializers.CharField(required=False, allow_blank=True)
