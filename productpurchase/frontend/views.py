import requests
from django.shortcuts import render
from django.http  import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from urllib.parse import urlparse
from django.urls import reverse
from json.decoder import JSONDecodeError
from . import utils
import json
from frontend.forms import OrderCreateForm


def index(request):
    return render(request, "frontend/index.html")


def product_listing(request):
    current_url = utils.get_domain_with_port (request.build_absolute_uri())
    try:
        response = requests.get(current_url  + "/products/")      
    except (requests.exceptions.RequestException, JSONDecodeError) as e:
        return render(request, 'frontend/index.html', {
            'error_message': e,
        })
    else:
        products = response.json()        
        return render(request, "frontend/product_listing.html", {"products": products})


def product_detail(request, product_id):
    current_url = utils.get_domain_with_port (request.build_absolute_uri())
    try:     
        response = requests.get(current_url  + "/products/" + str(product_id))  
        product = response.json()   
    except (requests.exceptions.RequestException, JSONDecodeError) as e:
        return render(request, 'frontend/index.html', {
            'error_message': e,
        })
    else:
        return render(request, 'frontend/product_detail.html', {'product': product })


def product_purchase(request, product_id):
    current_url = utils.get_domain_with_port (request.build_absolute_uri())
    response = requests.get(current_url  + "/products/" + str(product_id))  
    product = response.json()  
        
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            payload = utils.build_create_order_payload(form, product)
            order_confirmation = requests.post(current_url  + "/products/" + str(product_id) + "/purchase/", data = payload) 
            return render(request, 'frontend/purchase_complete.html', {'product': product, 'order_confirmation' : json.loads(order_confirmation.text) })
    else:
        form = OrderCreateForm()

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'frontend/product_purchase.html', context)