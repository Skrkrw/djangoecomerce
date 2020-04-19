from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all() # Return all the products that are in the DB
    return render(request, "products.html", {"products": products}) # Render products.html and accessing to all products