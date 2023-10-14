from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trip
from .serializers import TripSerializer


class TripList(APIView):
    """
    List Trip or create a trip if logged in
    The perform_create method associates the trip with the logged in user.
    """
    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(
            trips, many=True, context={'request': request}
        )
        return Response(serializer.data)

