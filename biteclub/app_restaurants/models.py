from django.db import models
from django.contrib.auth.models import User
from app_common.models import Address

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=75, unique=True)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='fallback.png', blank = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.name
    
class Menu_Item(models.Model):
    name = models.CharField(max_length=75, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default='fallback.png', blank = True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.name