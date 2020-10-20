from django.urls import path

from . import views

app_name="frontend"
urlpatterns = [
    path('', views.index, name='index'),
    path('product_listing', views.product_listing, name='product_listing'),
    path('product_listing/<int:product_id>/product_detail', views.product_detail, name='product_detail'),
    path('product_listing/<int:product_id>/product_purchase/', views.product_purchase, name='product_purchase')
]