from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from yacht_club_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Class ability: 
    List all profiles.
    No creating - handled by django signals.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Class ability: 
    Retrieve/ update a logged in profile.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer