from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'created_at', 'updated_at', 'name',
            'content', 'avatar', 'is_owner', 'following_id',
            'trips_count', 'followers_count', 'following_count',
        ]
