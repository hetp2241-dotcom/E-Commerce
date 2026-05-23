from django.contrib import admin
from ecommerce.apps.accounts.models import CustomerProfile, Address

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'created_at']
    search_fields = ['user__username', 'user__email']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'country', 'is_default']
    search_fields = ['user__username', 'city']
