from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trip
from .serializers import TripSerializer


class TripList(APIView):
    """
    List Trip or create a trip if logged in
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

