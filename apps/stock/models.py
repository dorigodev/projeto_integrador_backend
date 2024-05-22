from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    inStock = models.IntegerField(null=False, blank=False)
    available = models.BooleanField(default=True)
    stockDate = models.DateField(models.DateTimeField(default=datetime.now, null=True, blank=False))
    photo = models.ImageField(upload_to='products_photos/%Y/%m/%d/', blank=True, null=True)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')

    def __str__(self):
        return self.name

    def get_instock(self):
        return self.inStock

    def get_price(self):
        return self.price
