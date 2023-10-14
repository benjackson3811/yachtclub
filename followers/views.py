from rest_framework import generics, permissions
from yacht_club_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    Class ability:
    Create a follower (for logged on)
    Perform_create: associate the current logged in user with a follower.
    Lists followers of a user that is following other users
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Class ability:
    Retrieve follower details
    No update - Only follow or unfollow users
    Unfollow - Destroy a follower,
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer