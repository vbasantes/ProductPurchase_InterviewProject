"""productpurchase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
#from django.conf import settings
#from django.conf.urls.static import static
from rest_framework import routers
from products import views
from frontend import views

urlpatterns = [
    # URL route for admin site
    path('admin/', admin.site.urls),

    # URL route for products rest api
    path('products/',  include('products.urls')),                           #Not Versioned
    #re_path('products/(?P<version>(v1|v2))/', include('products.urls')),   #Versioned

    # URL route for frontend site
    path('',   include('frontend.urls')),
]
