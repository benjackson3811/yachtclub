from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trip
from .serializers import TripSerializer
from yacht_club_api.permissions import IsOwnerOrReadOnly


class TripList(APIView):
    """
    Logged in - List Trips / able to create a trip
    The perform_create method associates the trip with the logged in user.
    """
    serializer_class = TripSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(
            trips, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TripSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class TripDetail(APIView):
    serializer_class = TripSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try: 
            trip = Trip.objects.get(pk=pk)
            self.check_object_permissions(self.request, trip)
            return trip
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        trip = self.get_object(pk)
        serializer = TripSerializer(
            trip, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        trip = self.get_object(pk)
        serializer = TripSerializer(
            trip, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        trip = self.get_object(pk)
        trip.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
