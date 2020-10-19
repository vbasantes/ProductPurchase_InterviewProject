from django.contrib import admin
from .models import Product, Costumer, CostumerPhoneNumber, Order, Category, ProductType, PurchaseProduct

admin.site.site_header = "Product Purchase Admin"
admin.site.site_header = "Product Purchase Admin Area"
admin.site.index_title = "Welcome to the Product Purchase Admin Area" 

class PurchaseProductInline(admin.TabularInline):
    model = PurchaseProduct
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['order_confirmation']             }),
        (None,      {'fields': ['costumer'],    }),
        (None,      {'fields': ['order_total'],    }),
        ]
    inlines = [PurchaseProductInline]

admin.site.register(Product)
admin.site.register(Costumer)
admin.site.register(CostumerPhoneNumber)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductType)
admin.site.register(PurchaseProduct)