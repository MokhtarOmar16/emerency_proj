from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
# Create your models here.
class User(AbstractUser):
    objects = UserManager()
    
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    username = None
    REQUIRED_FIELDS = []