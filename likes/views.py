from rest_framework import generics, permissions
from yacht_club_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List likes or allows users to create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like/ delete id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
