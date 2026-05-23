from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce.apps.accounts.views import AuthViewSet, CustomerProfileViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'profile', CustomerProfileViewSet, basename='profile')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]
