from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title
