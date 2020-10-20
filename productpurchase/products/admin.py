from django.contrib import admin
from .models import Product, Customer, CustomerPhoneNumber, Order, Category, ProductType, PurchaseProduct

admin.site.site_header = "Product Purchase Admin"
admin.site.site_header = "Product Purchase Admin Area"
admin.site.index_title = "Welcome to the Product Purchase Admin Area" 

class PurchaseProductInline(admin.TabularInline):
    model = PurchaseProduct
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['customer'],    }),
        (None,      {'fields': ['order_total'],    }),
        ]
    inlines = [PurchaseProductInline]

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(CustomerPhoneNumber)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductType)
admin.site.register(PurchaseProduct)