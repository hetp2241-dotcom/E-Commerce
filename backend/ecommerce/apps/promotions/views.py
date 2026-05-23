from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ecommerce.apps.promotions.models import Coupon
from ecommerce.apps.promotions.serializers import CouponSerializer

class CouponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.filter(is_active=True)
    serializer_class = CouponSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def validate(self, request):
        code = request.data.get('code')
        try:
            coupon = Coupon.objects.get(code=code)
            if coupon.is_valid():
                return Response({
                    'valid': True,
                    'coupon': CouponSerializer(coupon).data
                })
            return Response({'valid': False, 'error': 'Coupon is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        except Coupon.DoesNotExist:
            return Response({'valid': False, 'error': 'Coupon not found'}, status=status.HTTP_404_NOT_FOUND)
