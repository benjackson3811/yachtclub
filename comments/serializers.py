from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment model Serializer
    Adds three extra fields when returning a list of Comment instances
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_avatar = serializers.ReadOnlyField(source='user.profile.avatar.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user
        
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
        
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
        
    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'is_user', 'profile_id', 'profile_avatar',
            'trip', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Detail view comment serializer, 
    Trip = read only field, no update needed on each comment/ update
    """
    trip = serializers.ReadOnlyField(source='trip.id')
