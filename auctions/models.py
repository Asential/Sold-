from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Comment(models.Model):
    name = models.CharField(max_length=64)
    item = models.CharField(max_length=64)
    comment = models.TextField(max_length=200)
    
    def __str__(self):
        return f"{self.name} commented on {self.item} - '{self.comment}'"

class Bid(models.Model):
    placer = models.CharField(max_length=64)
    item = models.CharField(max_length=64)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.placer} bid {self.amount}$ on {self.item}"
    

class Listing(models.Model):
    
    NONE = "None"
    FASHION = "Fashion"
    TOYS = "Toys"
    ELECTRONICS = "Electronics"
    HOME = "Home"

    CATEGORIES = [
        (NONE, "None"),
        (FASHION, "Fashion"),
        (TOYS, "Toys"),
        (ELECTRONICS, "Electronics"),
        (HOME, "Home")
    ]
    user = models.CharField(max_length=64)
    item = models.CharField(max_length=64)
    bid = models.IntegerField()
    description = models.TextField(max_length=600)
    category = models.CharField(choices=CATEGORIES, default=NONE, max_length=20)
    

    def __str__(self):
        return f"{self.item} : {self.category}"
     