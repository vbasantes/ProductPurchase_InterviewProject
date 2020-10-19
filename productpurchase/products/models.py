from django.db import models
import uuid


class ProductType(models.Model):
    type_name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.type_name


class Category(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(null=False, unique=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, default=None, null=True)
    cost = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    pushed_product = models.BooleanField()
    callback = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True)

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    inventory_on_hand = models.IntegerField(default=0)

    def __str__(self):
        return self.product


class CostumerPhoneNumber(models.Model):    
    number = models.IntegerField(default=0)
    
    PHONE_TYPE = (
        ('c', 'cell-phone'),
        ('w', 'work-phone'),
        ('a', 'home-phone'),
    )

    type = models.CharField(
        max_length=1,
        choices=PHONE_TYPE,
        blank=True,
        default='a',
        help_text='Phone types',
    )

    contact = models.BooleanField()

    def __str__(self):
        return str(self.number)


class Costumer(models.Model):    
    costumer_name = models.CharField(max_length=200)
    costumer_email = models.CharField(max_length=200)
    costumer_phone = models.ForeignKey(CostumerPhoneNumber, on_delete=models.SET_NULL, null=True)  

    def __str__(self):
        return self.costumer_name


class Order(models.Model):
    order_confirmation = models.IntegerField(primary_key=True)
    costumer = models.ForeignKey(Costumer, on_delete=models.SET_NULL, null=True)   
    order_total = models.FloatField()
 
    def __str__(self):
        return str(self.order_confirmation)


class PurchaseProduct(models.Model):    
    order_confirmation = models.ForeignKey(Order, to_field="order_confirmation", db_column="order_confirmation", on_delete=models.PROTECT)  
    code = models.ForeignKey(Product, to_field="code", db_column="code", on_delete=models.PROTECT)   
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.code)
 