from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from ecommerce.apps.shipping.models import ShippingMethod, Shipment
from ecommerce.apps.shipping.serializers import ShippingMethodSerializer, ShipmentSerializer

class ShippingMethodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShippingMethod.objects.filter(is_active=True)
    serializer_class = ShippingMethodSerializer
    permission_classes = [AllowAny]

class ShipmentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Shipment.objects.filter(order__user=self.request.user)
