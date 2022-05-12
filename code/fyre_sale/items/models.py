from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class SubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)



class ItemForSale(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_of_upload = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(default="photo.png", null=True, blank=True)
    condition = models.CharField(max_length=50)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    min_bid = models.IntegerField()
    cur_bid = models.IntegerField(default=0, blank=True)
    sold = models.BooleanField(default=False)
    long_desc = models.TextField(max_length=400)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])

class ItemImages(models.Model):
    item = models.ForeignKey(ItemForSale, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(default="favicon-fyresale.svg", null=True, blank=True)
    main_image = models.BooleanField(default=None, blank=True)

class Offer(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(ItemForSale, on_delete=models.CASCADE, blank=True)
    time_of_offer = models.DateTimeField(blank=True)
    price = models.IntegerField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    approved = models.BooleanField(default=None, blank=True)

    def __str__(self):
        return str(self.price)


class SoldItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemid = models.OneToOneField(ItemForSale, on_delete=models.CASCADE)
    offerid = models.OneToOneField(Offer, on_delete=models.CASCADE)
