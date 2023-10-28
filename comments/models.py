from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip


class Comment(models.Model):
    """
    Comment model, linked to User and Trip
    """
    user = models.ForeignKey(
        User, related_name='author',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='trip_comments',
        null=True, blank=True
    )
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
