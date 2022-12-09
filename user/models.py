from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    pin_code = models.CharField(max_length=8, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)


class users(AbstractUser):
    address = models.ForeignKey(Address, on_delete= models.CASCADE, null=True, blank=True, related_name='my_users_address' )
    type = models.CharField(max_length=50)