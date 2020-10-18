import requests
from django.shortcuts import render
from django.http  import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from urllib.parse import urlparse
from django.urls import reverse
from json.decoder import JSONDecodeError


def get_domain_with_port (complete_uri):
    parsed_uri = urlparse(complete_uri)
    domain_with_port = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return domain_with_port


def index(request):
    return render(request, "frontend/index.html")


def product_listing(request):
    current_url = get_domain_with_port (request.build_absolute_uri())
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
    current_url = get_domain_with_port (request.build_absolute_uri())
    try:     
        response = requests.get(current_url  + "/products/" + str(product_id) + "/details/")  
        product = response.json()   
    except (requests.exceptions.RequestException, JSONDecodeError) as e:
        return render(request, 'frontend/index.html', {
            'error_message': e,
        })
    else:
        return render(request, 'frontend/product_detail.html', {'product': product })


def product_purchase(request, product_id):
    current_url = get_domain_with_port (request.build_absolute_uri())
    try:     
        response = requests.get(current_url  + "/products/" + str(product_id) + "/details/")  
        product = response.json()   
    except (requests.exceptions.RequestException, JSONDecodeError) as e:
        return render(request, 'frontend/index.html', {
            'error_message': e,
        })
    else:
        return render(request, 'frontend/product_purchase.html', {'product': product })

def purchase_complete(request, product_id):
    current_url = get_domain_with_port (request.build_absolute_uri())
    try:
        product_response = requests.get(current_url  + "/products/" + str(product_id) + "/details/")  
        product = product_response.json()  

        order_response = requests.post(current_url  + "/products/" + str(product_id) + "/purchase/", 
            data = {'name':'testProduct'}) 
        order_confirmation = order_response.json()

        print (order_confirmation)
    except (requests.exceptions.RequestException, JSONDecodeError) as e:
        return render(request, 'frontend/index.html', {
            'error_message': e,
        })
    else:
        return render(request, 'frontend/purchase_complete.html', {'product': product, 'order_confirmation' : order_confirmation})
