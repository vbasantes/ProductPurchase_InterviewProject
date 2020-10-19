from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User, Group

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'code',
            'product_type',
            'cost',
            'description',
            'pushed_product',
            'callback',
            'category',
        )