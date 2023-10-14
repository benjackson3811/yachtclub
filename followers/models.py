from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, key fields 'user' and 'followed'.
    'user' = user whom is following.
    'followed' = User that is followed.
    """
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE, null=True, blank=True)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'followed']
        
    def __str__(self):
        	     return f'{self.user} {self.followed}'