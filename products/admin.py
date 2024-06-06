from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ( 
        'sku', 
        'name', 
        'category', 
        'price',
        'rating',
        'image',
    )

    # Change how things are ordered in the admin panel:
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register everything here at the end:

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)