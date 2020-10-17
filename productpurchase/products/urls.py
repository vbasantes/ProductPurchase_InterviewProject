from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [

    #This blank '' means polls index page
    path('', views.index, name='index'),
]