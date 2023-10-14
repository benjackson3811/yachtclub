from rest_framework import serializers
from trips.models import Trip
from likes.models import Like


class TripSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    avatar = serializers.ReadOnlyField(source='user.profile.avatar.url')
            
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Trip
        fields = ['id', 'user', 'is_user', 'profile_id', 
        'avatar', 'created_at', 'updated_at', 'trip_title',
        'description', 'image', 'category', 'trip_categories' ]
