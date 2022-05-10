from django.db import models
from django.contrib.auth.models import User
from items.models import Offer


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
    expires = models.DateField(default=None, max_length=5)
    cvc = models.CharField(default=None, max_length=4)

class User_rating(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_rating = models.IntegerField(default=None)

class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(blank=True)














