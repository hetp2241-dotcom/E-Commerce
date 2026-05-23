from django.contrib import admin
from ecommerce.apps.support.models import SupportTicket

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ['subject', 'user', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['subject', 'user__username']
