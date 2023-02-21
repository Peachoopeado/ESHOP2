from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_product_list, name="product-list"),
    path('<int:category_id>', views.show_product_list, name='product-list-by-category'),
    path('<int:product_id>',views.show_product_detail, name="product-detail")
]
