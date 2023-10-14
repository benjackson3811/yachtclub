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

class TripDetailViewTests(APITestCase):
    def setUp(self):
        ben = User.objects.create_user(username='ben', password='pass')
        ten = User.objects.create_user(username='ten', password='pass')
        Trip.objects.create(
            user=ben, trip_title='a title', description='bens content'
        )
        Trip.objects.create(
            user=ten, trip_title='the title', description='tens content'
        )

    def test_can_retrieve_trip_using_valid_id(self):
        response = self.client.get('/trips/1/')
        self.assertEqual(response.data['trip_title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_trip_using_invalid_id(self):
        response = self.client.get('/trip/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_trip(self):
        self.client.login(username='ben', password='pass')
        response = self.client.put('/trips/1/', {'trip_title': 'a new title'})
        trip = Trip.objects.filter(pk=1).first()
        self.assertEqual(trip.trip_title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_trip(self):
        self.client.login(username='ten', password='pass')
        response = self.client.put('/trips/1/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)