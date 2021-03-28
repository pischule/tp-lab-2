from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    class Types(models.TextChoices):
        BUYER = 'BUYER', 'Buyer'
        SELLER = 'SELLER', 'Seller'

    type = models.CharField(max_length=50, choices=Types.choices, default=Types.BUYER)
    address = models.CharField(max_length=200)


class BuyerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.BUYER)


class SellerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SELLER)


class Buyer(User):
    objects = BuyerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.BUYER
        return super().save(*args, **kwargs)


class Seller(User):
    objects = SellerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.SELLER
        return super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:product-detail', args=[str(self.id)])


class ProductInstance(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField()

    def __str__(self):
        return str(self.product) + ' -- ' + str(self.count)


class Order(models.Model):
    class Status(models.TextChoices):
        CREATED = 'CREATED', 'Created'
        DELIVERED = 'DELIVERED', 'Delivered'

    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.CREATED)
    placed_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return sum([i.product.price * i.count for i in OrderItem.objects.filter(order_id=self.id)])

    def __str__(self):
        return f'O:{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField()
