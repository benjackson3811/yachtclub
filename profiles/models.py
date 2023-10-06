rom django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_profile')
    display_name= models.Charfield(max_length=25, null=True, blank=True, related_name='user_profile')
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='images/', default='../default_profile_udonlm', blank=True)

    class Meta:
		ordering = [‘-created_at’]

    def__str__(self):
		return f”{self.owners}’s profile”

def create_profile(sender, instance , created, **kwargs):
    If created:
	    Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
