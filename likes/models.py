from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip


class Like(models.Model):
    """
    Like model, linked to 'owner' and trip.
    'owner' is a User instance and 'trip' is a Post instance.
    'unique_together' makes sure a user can't like the same trip twice.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    trip = models.ForeignKey(Trip, related_name='likes', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'trip']
        
    def __str__(self):
        return f'{self.owner} {self.trip}'
