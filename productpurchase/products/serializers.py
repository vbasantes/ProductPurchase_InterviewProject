from rest_framework import serializers
from .models import Product, ProductType, Order, Category, CustomerPhoneNumber, PurchaseProduct
from django.contrib.auth.models import User, Group


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        depth = 1
        fields = (
            'type_name',
            'type',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        depth = 1
        fields = (
            'name',
            'type',
        )


class ProductSerializer(serializers.ModelSerializer):

    product_type = ProductTypeSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        depth = 1
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


class ProductDetailsSerializer(serializers.ModelSerializer):

    product_type = ProductTypeSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        depth = 1
        fields = (
            'name',
            'code',
            'product_type',
            'cost',
            'description',
            'pushed_product',
            'callback',
            'category',
        )


class CustomerPhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerPhoneNumber
        fields = (
            'number',
            'type',
            'contact',
        )


class PurchaseProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseProduct
        fields = (
            'code',
            'quantity',
        )


class OrderConfirmationSerializer(serializers.ModelSerializer):

    customer_name = serializers.SerializerMethodField('get_customer_name')
    customer_email = serializers.SerializerMethodField('get_customer_email')
    customer_phone = serializers.SerializerMethodField('get_customer_phone')
    purchase_products = serializers.SerializerMethodField('get_purchase_products')

    class Meta:
        model = Order
        depth = 1
        fields = (
            "order_confirmation",
            "customer_name",
            "customer_email",
            "customer_phone",
            "purchase_products",
	        "order_total",
        )

    def get_customer_name(self, obj):
        return obj.customer.customer_name
        
    def get_customer_email(self, obj):
        return obj.customer.customer_email
        
    def get_customer_phone(self, obj):
        serialize = CustomerPhoneNumberSerializer(obj.customer.customer_phone)
        return serialize.data

    def get_purchase_products(self, obj):
        serialize = PurchaseProductSerializer()
        return serialize.data