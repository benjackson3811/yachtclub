from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'created_at', 'updated_at', 'display_name',
            'bio', 'avatar'
        ]
