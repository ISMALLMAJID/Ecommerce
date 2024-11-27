import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AssipaFood')
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('is admin', default=False)
    is_stuff = models.BooleanField('is stuff', default=False)
    is_customer = models.BooleanField('is customer', default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='images_users/', blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank= True, null=True)
    def __str__(self):
        return self.username

    