from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from yacht_club_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Class ability: 
    List all profiles.
    No creating - handled by django signals.
    """
    queryset = Profile.objects.annotate(
        trips_count=Count('user__trip_post', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'user__followed',
        'user_following'
    ]
    ordering_fields = [
        'trips_post_count',
        'followers_count',
        'following_count',
        'user__following__created_at',
        'user__followed__created_at',
    ]

 
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Class ability: 
    Retrieve/ update a logged in profile.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        trips_count=Count('user__trip_post', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer