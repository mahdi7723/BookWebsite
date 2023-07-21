from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
