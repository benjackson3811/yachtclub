from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip

class Comment(models.Model):
    """
    Comment model, linked to User and Trip
    """
    user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.content
