from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from homepage.models import Customer
from homepage.forms  import CustomerForm



# Create your views here.
def customer_requests(request):
    customer_request = Customer.objects.all()

    return render(request, 'index.html',{'customer_request':customer_request  })

def company_input_form(request):
    if request == "POST":
        form = CustomerForm
        if form.is_valid():
            data = cleaned_data
            new_request = Customer.objects.create(
                company_name = data[company_name],
                website_needs = data[website_needs],
                email = data[email]
            )
        return HttpResponseRedirect(reverse('Home'))
    form = CustomerForm()
    return render(request, "generic_form.html", {"form": form})