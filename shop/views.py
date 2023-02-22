from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def show_category_list(request):
    categories = models.Category.objects.all()
    data = {
        'categories': categories,
    }

    return render(request, 'shop/categories.html', data)

def show_product_list(request, category_slug = None):
    category = None
    categories = models.Category.objects.all()
    vehic_types = models.VehicleType.objects.all()
    oil_types = models.OilType.objects.all()
    viscosity = models.Viscosity.objects.all()
    transmission = models.Transmission.objects.all()
    compound = models.Compound.objects.all()
    fuel = models.Fuel.objects.all()
    products = models.Product.objects.all()
    if category_slug:
        category = get_object_or_404(models.Category, slug=category_slug)
        products = models.Product.objects.filter(category=category)

    data = {
        'category': category,
        'categories': categories,
        'vehic_types': vehic_types,
        'oil_types': oil_types,
        'visc': viscosity,
        'transmission': transmission,
        'compound': compound,
        'fuel': fuel,
        'products': products,
    }

    return render(request, f'shop/{category_slug}.html', data)





def show_product_detail(request, product_id: int):
    product = get_object_or_404(models.Product, id=product_id)
    data = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', data)
