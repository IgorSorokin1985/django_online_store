from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import NULLABLE

# Create your models here.

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Phone number', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Country', **NULLABLE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
