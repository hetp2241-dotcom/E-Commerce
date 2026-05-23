from rest_framework import serializers
from ecommerce.apps.reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'product', 'rating', 'title', 'comment', 'user_name', 'helpful_count', 'created_at']
        read_only_fields = ['helpful_count', 'created_at']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'title', 'comment']
