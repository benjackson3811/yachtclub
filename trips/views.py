from rest_framework import generics, permissions
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
    queryset = Trip.objects.all()

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
    queryset = Trip.objects.all()