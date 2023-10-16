from rest_framework import serializers
from trips.models import Trip
from likes.models import Like
from profiles.models import Profile


class TripSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    avatar = serializers.ReadOnlyField(source='user.profile.avatar.url')
    like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 *2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
        )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
        )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
        )
        return value
      
    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                user=user, trip=obj
            ).first()
            return like.id if like else None
        return None


    class Meta:
        model = Trip
        fields = ['id', 'user', 'is_user', 'profile_id', 
        'avatar', 'created_at', 'updated_at', 'trip_title',
        'description', 'image', 'category', 'like_id', ]
