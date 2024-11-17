from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)