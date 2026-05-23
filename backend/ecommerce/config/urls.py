from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('ecommerce.apps.accounts.urls')),
    path('api/products/', include('ecommerce.apps.catalog.urls')),
    path('api/cart/', include('ecommerce.apps.cart.urls')),
    path('api/checkout/', include('ecommerce.apps.checkout.urls')),
    path('api/orders/', include('ecommerce.apps.orders.urls')),
    path('api/payments/', include('ecommerce.apps.payments.urls')),
    path('api/shipping/', include('ecommerce.apps.shipping.urls')),
    path('api/promotions/', include('ecommerce.apps.promotions.urls')),
    path('api/reviews/', include('ecommerce.apps.reviews.urls')),
    path('api/support/', include('ecommerce.apps.support.urls')),
    path('api/analytics/', include('ecommerce.apps.analytics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
