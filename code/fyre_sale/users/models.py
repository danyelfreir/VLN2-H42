from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(default=None, max_length=255)
    email = models.CharField(default=None, max_length=255)
    bio = models.TextField(default=None, max_length=9999)
    birthday = models.CharField(default=None, max_length=255)
    joindate = models.CharField(default=None, max_length=255)
    profileimg = models.TextField(blank=True, null=True, max_length=9999)
