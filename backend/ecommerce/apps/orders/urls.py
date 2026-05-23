from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce.apps.orders.views import OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', OrderViewSet.as_view({'post': 'create_order'}), name='order-create'),
]
