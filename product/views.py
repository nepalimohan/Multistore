from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
def home(request):
    category = models.Category.objects.all()
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
    product = models.Product.objects.filter(category__id=id)
    context = {
        'product': product,
    }
    
    return render(request, 'product/shop.html', context)

@login_required(login_url='/account/login/')
def cart(request):
    return render(request, 'product/cart.html')

def plus_cart(request):
    pass

def minus_cart(request):
    pass

# @login_required(login_url='/account/login/')
def checkout(request):
    return render(request, 'product/checkout.html')