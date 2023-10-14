from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile',
        null=True, blank=True)
    display_name= models.CharField(max_length=25, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    avatar = models.ImageField(
        upload_to='avatars/', default='../default_profile_udonlm',
        null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.user}'s profile"
    
"""
signal for the creation of the profile
"""
def create_profile(sender, instance , created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
            
            
post_save.connect(create_profile, sender=User)
