from django.urls import path
from ecommerce.apps.checkout.views import CheckoutViewSet

urlpatterns = [
    path('validate/', CheckoutViewSet.as_view({'post': 'validate'}), name='checkout-validate'),
]
