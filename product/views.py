from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def products(request, id):
    product = models.Product.objects.filter(subcategory__id=id)
    print(product)
    context = {
        'product': product,
    }
    
    return HttpResponse("Dynamic")


def shop(request):
    return render(request, 'product/shop.html')

def checkout(request):
    return render(request, 'product/checkout.html')