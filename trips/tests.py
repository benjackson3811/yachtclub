from django.contrib.auth.models import User
from .models import Trip
from rest_framework import status
from rest_framework.test import APITestCase

class TripListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='ben', password='pass')

    def test_can_list_trips(self):
        ben = User.objects.get(username='ben')
        Trip.objects.create(user=ben, trip_title='a trip')
        response = self.client.get('/trips/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_trip(self):
        self.client.login(username='ben', password='pass')
        response = self.client.post('/trips/', {'trip_title': 'a title'})
        count = Trip.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_in_user_cant_create_trip(self):
        response = self.client.post('/trips/', {'trip_title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)