from django.db import models
from users.models import User


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.TextField(blank=True, null=True, max_length=9999)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItemForSale(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.TextField(blank=True, null=True, max_length=9999)
    condition = models.CharField(max_length=255)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    time_of_upload = models.CharField(max_length=255)
    date_of_upload = models.CharField(max_length=255)
    min_bid = models.IntegerField()
    cur_bid = models.IntegerField()
    sold = models.BooleanField()
    long_desc = models.TextField(max_length=9999)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Offer(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(ItemForSale, on_delete=models.CASCADE)
    time_of_offer = models.DateTimeField()
    price = models.FloatField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.price


class SoldItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(ItemForSale, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
