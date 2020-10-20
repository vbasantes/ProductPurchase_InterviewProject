from django import forms
    
PHONE_TYPES = [
    ('h', 'Homephone'),
    ('c', 'Cellphone'),
    ('w', 'Workphone'),
]

class OrderCreateForm(forms.Form):
    
    product_quantity = forms.IntegerField()

    customer_email = forms.CharField(widget=forms.TextInput(attrs={'class' : '', 'placeholder' : "Enter Customer Email"}))
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'class' : '', 'placeholder' : "Enter Customer Name"}))

    customer_phone_number = forms.IntegerField()
    customer_phone_type = forms.ChoiceField(widget=forms.Select, choices=PHONE_TYPES)
    customer_phone_contact = forms.BooleanField(required=False)
    
    shipping_address_street = forms.CharField(widget=forms.TextInput(attrs={'class' : '', 'placeholder' : "Enter Shipping Address Street"}))
    shipping_address_city = forms.CharField(widget=forms.TextInput(attrs={'class' : '', 'placeholder' : "Enter Shipping Address City"}))
    shipping_address_state = forms.CharField(widget=forms.TextInput(attrs={'class' : '', 'placeholder' : "Enter Shipping Address State"}))
    shipping_address_zipcode = forms.IntegerField()
    
    billing_address_street = forms.CharField(widget=forms.TextInput(attrs={'class' : '', 'placeholder' : "Enter Billing Address Street"}))
    billing_address_city = forms.CharField(widget=forms.TextInput(attrs={'class' : '', 'placeholder' : "Enter Billing Address City"}))
    billing_address_state = forms.CharField(widget=forms.TextInput(attrs={'class' : '', 'placeholder' : "Enter Billing Address State"}))
    billing_address_zipcode = forms.IntegerField()