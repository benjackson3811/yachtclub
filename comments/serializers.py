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
    avatar = serializers.ReadOnlyField(source='user.profile.avatar.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'is_user', 'profile_id', 'profile_avatar',
            'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Trip is a read only field, not update needed on each update
    """
    trip = serializers.ReadOnlyField(source=trip.id')
