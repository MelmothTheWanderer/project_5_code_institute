from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404

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

def product_detail(request, product_id):
    """
    A view that displays the details of an individual product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = { 
        'product' : product
    }

    return render(request, 'products/product_details.html', context)

