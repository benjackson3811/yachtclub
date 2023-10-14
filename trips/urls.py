from django.urls import path
from trips import views

urlpatterns = [
    path('trips/', views.TripList.as_view())
]