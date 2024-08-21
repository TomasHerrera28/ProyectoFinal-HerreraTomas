from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    
class Client(models.Model):
    user = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
class Cart(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    sold = models.BooleanField()