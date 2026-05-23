from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ecommerce.apps.analytics.models import PageView
from ecommerce.apps.analytics.serializers import PageViewSerializer

class PageViewViewSet(viewsets.ModelViewSet):
    queryset = PageView.objects.all()
    serializer_class = PageViewSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def track_page(self, request):
        page = request.data.get('page')
        session = request.data.get('session_id', '')
        PageView.objects.create(page=page, user_session=session)
        return Response({'success': True})
