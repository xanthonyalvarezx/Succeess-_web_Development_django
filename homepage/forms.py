from django import forms
from django.forms import ModelForm
from homepage.models import Customer

class CustomerForm(ModelForm):
    class Meta:
       model = Customer
       fields = ['company_name', 'website_needs', 'email']