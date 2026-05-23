from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ecommerce.apps.support.models import SupportTicket
from ecommerce.apps.support.serializers import SupportTicketSerializer

class SupportTicketViewSet(viewsets.ModelViewSet):
    serializer_class = SupportTicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SupportTicket.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
