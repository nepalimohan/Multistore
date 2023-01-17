from django.shortcuts import render, redirect
from . import models

# Create your views here.
def products(request, id):
    product = models.Product.objects.filter(subcategory__id=id)
    print(product)


def shop(request):
    return render(request, 'product/shop.html')

def checkout(request):
    return render(request, 'product/checkout.html')