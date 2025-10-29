from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from .models import Product, ProductImage
from django.views.generic import (CreateView, ListView, 
                                  DetailView, UpdateView, DeleteView)

# -----------Product CRUD-----------------
class AddProduct(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/add_product.html'
    success_url = reverse_lazy("view_products")

class ViewProducts(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products.html'

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_details.html'
    