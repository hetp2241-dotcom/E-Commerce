from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce.apps.analytics.views import PageViewViewSet

router = DefaultRouter()
router.register(r'pageviews', PageViewViewSet, basename='pageview')

urlpatterns = [
    path('', include(router.urls)),
]
