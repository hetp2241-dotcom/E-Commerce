from django.urls import path
from ecommerce.apps.cart.views import CartViewSet

cart_view = CartViewSet.as_view({
    'get': 'current',
    'post': 'add_item',
})

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/', CartViewSet.as_view({'post': 'add_item'}), name='cart-add'),
    path('remove/', CartViewSet.as_view({'post': 'remove_item'}), name='cart-remove'),
    path('update/', CartViewSet.as_view({'post': 'update_item'}), name='cart-update'),
    path('clear/', CartViewSet.as_view({'post': 'clear'}), name='cart-clear'),
]
