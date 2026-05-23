from django.contrib import admin
from ecommerce.apps.shipping.models import ShippingMethod, Shipment

@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'estimated_days', 'is_active']
    list_filter = ['is_active']

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['order', 'status', 'tracking_number', 'shipped_date']
    list_filter = ['status', 'shipped_date']
    search_fields = ['tracking_number', 'order__order_number']
