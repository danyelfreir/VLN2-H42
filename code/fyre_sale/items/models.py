from django.db import models

# Create your models here.

class ItemForSale(models.Model):
    self.id = models.BigAutoField()
    self.name = models.CharField(max_length=255)
