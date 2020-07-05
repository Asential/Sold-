from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    status = models.BooleanField(default=True)
    item = models.CharField(max_length=64)
    startbid = models.IntegerField()
    description = models.TextField(max_length=600)
    image_url = models.CharField(max_length=300, blank=True)
    category = models.CharField(choices=CATEGORIES, default=NONE, max_length=20)
    

    def __str__(self):
        return f"{self.item} : {self.category}"
     

class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    
    def __str__(self):
        return f"{self.name} commented on {self.item} - '{self.comment}'"

class Bid(models.Model):
    placer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.placer} bid {self.amount}$ on {self.item}"

class WishList(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Listing, blank=True, related_name="items")
    def __str__(self):
        return f"{self.name}"