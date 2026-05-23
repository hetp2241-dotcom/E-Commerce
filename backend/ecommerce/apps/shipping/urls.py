from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce.apps.shipping.views import ShippingMethodViewSet, ShipmentViewSet

router = DefaultRouter()
router.register(r'methods', ShippingMethodViewSet, basename='shipping-method')
router.register(r'shipments', ShipmentViewSet, basename='shipment')

urlpatterns = [
    path('', include(router.urls)),
]
