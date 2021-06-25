from django.urls import path
from homepage.views import customer_requests, company_input_form
urlpatterns = [
     path('', customer_requests, name='Home'  ),
     path('input_form/', company_input_form, name='company_input_form'  ),
]
