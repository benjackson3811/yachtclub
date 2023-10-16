from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Trip
from .serializers import TripSerializer
from yacht_club_api.permissions import IsOwnerOrReadOnly


class TripList(generics.ListCreateAPIView):
    """
    Class ability:
    Create posts/ list created trips
    trips are associates the trip with the logged in user.
    """
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Trip.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('trip_comments', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = [
        'user__followed__user__profile',
        'likes__user__profile',
        'user__profile',
    ]
    search_fields = [
        'user__username',
        'trip_title',
    ]
    ordering_fields = [
        'likes_count',
        'trip_comments_count',
        'likes__created_at',
    ]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Class ability:
    Retrieve a post,
    Edit,
    Delete it if you own it.
    """
    serializer_class = TripSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Trip.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('trip_comments', distinct=True)
    ).order_by('-created_at')