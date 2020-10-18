from django.contrib import admin

# Register your models here.
from .models import Product, Costumer

admin.site.register(Product)
admin.site.register(Costumer)