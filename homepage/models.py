from django.db import models

# Create your models here.
class Customer(models.Model):
    company_name = models.CharField( max_length=50)
    website_needs = models.TextField()
    email = models.EmailField( max_length=254)
def  __str__(self):
    return self.company_name
