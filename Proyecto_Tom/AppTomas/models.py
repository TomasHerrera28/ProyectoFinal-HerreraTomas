from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    
class Cliente(models.Model):
    user = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
class Carrito(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    vendido = models.BooleanField()