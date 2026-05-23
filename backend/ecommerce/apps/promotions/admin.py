from django.contrib import admin
from ecommerce.apps.promotions.models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_type', 'discount_value', 'is_active', 'current_uses']
    list_filter = ['is_active', 'discount_type']
    search_fields = ['code']
