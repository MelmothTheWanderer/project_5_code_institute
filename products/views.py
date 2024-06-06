from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def all_products(request):
    """
    A view that shows all of the products, with sorting and search queries
    """
    products = Product.objects.all()

    context = { 
        'products' : products
    }

    return render(request, 'products/products.html', context)
