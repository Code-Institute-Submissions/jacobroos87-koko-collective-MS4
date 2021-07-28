from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username
