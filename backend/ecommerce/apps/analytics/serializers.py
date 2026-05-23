from rest_framework import serializers
from ecommerce.apps.analytics.models import PageView

class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageView
        fields = ['id', 'page', 'viewed_at']
