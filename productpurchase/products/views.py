from django.template import loader
from django.http  import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets, permissions, generics
from . import models
from . import serializers
from .models import Product, Order, Customer, CustomerPhoneNumber
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import json


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @action(methods=['post'], detail=True, url_path='purchase', url_name='purchase')
    def purchase(self, request, pk=None):
        order_create_payload = json.loads(request.body)

        if order_create_payload != None:

            customerphonenumber =  CustomerPhoneNumber.objects.create(
                                            number = order_create_payload['customer_phone'][0]['number'],
                                            type= order_create_payload['customer_phone'][0]['type'],
                                            contact= order_create_payload['customer_phone'][0]['contact'])
            customer = Customer.objects.create(
                                            customer_name = order_create_payload['customer_name'], 
                                            customer_email= order_create_payload['customer_email'], 
                                            customer_phone= customerphonenumber)
            order = Order.objects.create(customer = customer, order_total=0)

            total = 0
            for purchaseproduct in order_create_payload['purchase_products']:
                product = Product.objects.get(code=purchaseproduct['code'])
                total += product.cost * purchaseproduct['quantity'] 
                order.purchaseproduct_set.create(code=product, quantity=purchaseproduct['quantity'])
            
            #Update order_total
            order.order_total = total
            order.save()

            order_confirmation_serializer = serializers.OrderConfirmationSerializer(order)
            return Response(order_confirmation_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(order_create_payload.errors, status=status.HTTP_400_BAD_REQUEST)
            

    @action(detail=True, url_path='details', url_name='details')
    def details(self, request, pk=None):
        p = self.get_object()
        serializer = serializers.ProductDetailsSerializer(p)
        if p != None:
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)