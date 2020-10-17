from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Costumer(models.Model):
    customer_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.customer_name
        