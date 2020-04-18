from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product) # Reg product > models.py > Product to be able to add products through the admin panel
