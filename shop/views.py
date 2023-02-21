from django.shortcuts import render
from . import models

# Create your views here.
def show_product_list(request):
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    data = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'shop/product_list.html', data)