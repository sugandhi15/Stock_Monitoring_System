from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=128)




class Stock(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

