from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    imagen = models.ImageField(upload_to='products', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return "{} | ID: {}".format(self.name, self.id)
    

    