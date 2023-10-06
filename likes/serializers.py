from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Like model Serializer
    The create method handles the unique constraint on 'owner' and ‘trip’
    """
    
    user = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'trip']
        
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
                })
