from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_path = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    last_activity = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user
    
