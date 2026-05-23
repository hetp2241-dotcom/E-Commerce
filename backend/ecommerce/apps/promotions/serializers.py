from rest_framework import serializers
from ecommerce.apps.promotions.models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    is_valid_coupon = serializers.SerializerMethodField()

    class Meta:
        model = Coupon
        fields = ['id', 'code', 'discount_type', 'discount_value', 'min_order_amount', 'is_valid_coupon']

    def get_is_valid_coupon(self, obj):
        return obj.is_valid()
