from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class User(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    name = models.CharField(default=None, max_length=255)
#    email = models.CharField(default=None, max_length=255)
#    bio = models.TextField(default=None, max_length=9999)
#    birthday = models.CharField(default=None, max_length=255)
#    joindate = models.CharField(default=None, max_length=255)
#   profileimg = models.TextField(blank=True, null=True, max_length=9999)

class User_info(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profileimg = models.TextField(blank=True, null=True, max_length=9999)
    bio = models.TextField(default=None, max_length=9999)
    birthday = models.CharField(default=None, max_length=255)

class Address_info(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street_name = models.CharField(default=None, max_length=255)
    zip = models.CharField(default=None, max_length=15)
    city = models.CharField(default=None, max_length=255)
    country = models.CharField(default=None, max_length=255)

class Payment_info(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    card_nr = models.CharField(default=None, max_length=20)
    expires = models.CharField(default=None, max_length=5)
    cvc = models.IntegerField(default=None)

class User_rating(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_rating = models.IntegerField(default=None)