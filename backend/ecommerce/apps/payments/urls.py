from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce.apps.payments.views import PaymentViewSet

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('process/', PaymentViewSet.as_view({'post': 'process_payment'}), name='payment-process'),
]
