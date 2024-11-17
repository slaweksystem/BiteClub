from django.db import models
from django.contrib.auth.models import User

from app_restaurants.models import Menu_Item
from app_common.models import Address
from app_restaurants.models import Restaurant

# Create your models here.
class Dinner_Session(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_expires = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Dinner_Session_Item(models.Model):
    food_item = models.ForeignKey(Menu_Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user_comments = models.CharField(blank=True, max_length=200)
    dinner_session = models.ForeignKey(Dinner_Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_item.name

class Dinner_Session_Restaurants(models.Model):
    dinner_session = models.ForeignKey(Dinner_Session, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
