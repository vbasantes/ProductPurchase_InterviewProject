from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet
from . import views

router = DefaultRouter()
router.register('', ProductsViewSet, basename='products') 

app_name = 'products'
urlpatterns = [
    path('', include(router.urls)),
]