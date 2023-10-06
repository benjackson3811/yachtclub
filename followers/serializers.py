from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Follower model Serializer
    Create method handles the unique constraint on 'owner' and 'followed'
    """
    user = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')
    
    class Meta:
        model = Follower
        fields = [
            'id', 'user', 'created_at', 'followed', 'followed_name'
        ]
        
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
