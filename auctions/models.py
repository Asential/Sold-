from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Comment(models.Model):
    first = models.CharField(max_length=64)
    comment = models.TextField(max_length=200)

    