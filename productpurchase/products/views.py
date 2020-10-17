from django.template import loader
from django.http  import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets, permissions, generics
from . import models
from . import serializers
from .models import Product, Costumer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
 
    @action(methods=['post'], detail=True, url_path='purchase', url_name='purchase')
    def purchase(self, request, pk=None):
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            p = Product(name = serializer.data['name'])
            p.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, url_path='details', url_name='details')
    def details(self, request, pk=None):
        p = self.get_object()
        serializer = serializers.ProductSerializer(p)
        if p != None:
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)