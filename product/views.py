from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def home(request):
    category = models.Category.objects.all().distinct()
    subcategory = models.Subcategory.objects.all().distinct()
    product = models.Product.objects.all().last()
    # print(product.)
    product = {
        'category':category,
        'subcategory':subcategory,
        'product':product,
    }
    return render(request, 'product/home.html', product)

def products(request, id):
    product = models.Product.objects.filter(subcategory__id=id)
    context = {
        'product': product,
    }
    
    return render(request, 'product/shop.html', context)
    # return HttpResponse("Dynamic")


def shop(request, id):
    product = models.Product.objects.filter(subcategory__id=id)
    context = {
        'product': product,
    }
    
    return render(request, 'product/shop.html', context)

def cart(request):
    return render(request, 'product/cart.html')

def checkout(request):
    return render(request, 'product/checkout.html')