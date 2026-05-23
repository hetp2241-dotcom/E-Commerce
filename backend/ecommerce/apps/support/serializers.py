from rest_framework import serializers
from ecommerce.apps.support.models import SupportTicket

class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = ['id', 'subject', 'message', 'status', 'created_at', 'updated_at']
