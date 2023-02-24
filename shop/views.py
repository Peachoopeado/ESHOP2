from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def show_category_list(request):
    categories = models.Category.objects.all()
    data = {
        'categories': categories,
    }

    return render(request, 'shop/categories.html', data)

def show_product_list(request, category_id = None):
    category = None
    filts = models.Filter.objects.all()
    products = models.Product.objects.all()
    if category_id:
        category = get_object_or_404(models.Category, id=category_id)
        filts = get_object_or_404(models.Filter, id=category_id)
        products = models.Product.objects.filter(category=category)

    data = {
        'category': category,
        'filts': filts,
        'products': products,
    }

    return render(request, f'shop/product_list.html', data)





def show_product_detail(request, product_id: int):
    product = get_object_or_404(models.Product, id=product_id)
    data = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', data)
