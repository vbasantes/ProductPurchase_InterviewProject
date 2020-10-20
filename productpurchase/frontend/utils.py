from urllib.parse import urlparse
import json

def get_domain_with_port (complete_uri):
    parsed_uri = urlparse(complete_uri)
    domain_with_port = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return domain_with_port


def build_create_order_payload (form, product):

    create_order_payload = {
        "customer_name":form.cleaned_data['customer_name'],
        "customer_email":form.cleaned_data['customer_email'],
        "customer_phone":[
            {
                "number":form.cleaned_data['customer_phone_number'], 
                "type":form.cleaned_data['customer_phone_type'],
                "contact":form.cleaned_data['customer_phone_contact']
            }
        ],
        "shipping_address":[
            {
                "street":form.cleaned_data['shipping_address_street'],
                "city":form.cleaned_data['shipping_address_street'],
                "state":form.cleaned_data['shipping_address_street'],
                "zipcode":form.cleaned_data['shipping_address_street']
            }
        ],
        "billing_address":[
            {
                "street":form.cleaned_data['billing_address_street'],
                "city":form.cleaned_data['billing_address_city'],
                "state":form.cleaned_data['billing_address_state'],
                "zipcode":form.cleaned_data['billing_address_zipcode']
            }
        ],
        "purchase_products":[
            {
                "code":product['code'],
                "quantity":form.cleaned_data['product_quantity']
            }
        ]
    }
    
    return(json.dumps(create_order_payload))

