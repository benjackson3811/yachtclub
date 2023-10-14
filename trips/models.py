from django.db import models
from django.contrib.auth.models import User


TRIP_CATEGORIES = (
        ("1", "Fleet"),
        ("2", "Racing"),
        ("3", "Parasailing"),
        ("4", "eSailing"),
        ("5", "Offshore"),
        ("6", "Cruising"),
        ("7", "Radio"),
    )


class Trip(models.Model):
    """
    Trip model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    user  = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='trip_post')
    trip_title = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_trip_b4mj7o', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=255, blank=False, choices=TRIP_CATEGORIES, default='Sightseeing'
        )
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.id} {self.title}'
