from django import forms
from django.db import models

from . models import ShippingAddress

class ShippingAddress(models.Model):
    
    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'email','address1', 'address2', 'city', 'state', 'zipcode']
        exclude = ['user',]