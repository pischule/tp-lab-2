from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    BUYER = 'b'
    SELLER = 's'

    USER_TYPE_CHOICES = [
        (BUYER, 'buyer'),
        (SELLER, 'seller')
    ]

    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=1, default=BUYER)

    def __str__(self):
        return self.username
