from django.shortcuts import render
from django.views import generic

from . import models

class ProductList(generic.ListView):
    queryset=models.Product.objects.filter(status=True)
    template_name='products/product_list.html'
    context_object_name='products'
    
class ProductDetail(generic.DetailView):
    model=models.Product
    template_name='products/product_detail.html'
    context_object_name='product'
    
    
    