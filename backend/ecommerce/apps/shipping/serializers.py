from rest_framework import serializers
from ecommerce.apps.shipping.models import ShippingMethod, Shipment

class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = ['id', 'name', 'description', 'cost', 'estimated_days']

class ShipmentSerializer(serializers.ModelSerializer):
    shipping_method = ShippingMethodSerializer(read_only=True)

    class Meta:
        model = Shipment
        fields = ['id', 'order', 'shipping_method', 'tracking_number', 'status', 'shipped_date', 'delivered_date']
