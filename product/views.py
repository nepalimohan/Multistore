from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from .models import Cart
from django.shortcuts import get_object_or_404

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

# @login_required(login_url='/account/login/')
def cart(request):
    # user= request.user
    # product_id = request.GET.get('prod_id')
    # print(product_id)
    # product = models.Product.objects.get(id=product_id)
    
    # models.Cart.objects.create(user=user, product=product)
    # return redirect('product:cart')
    cart = models.Cart.objects.all()
    context = {
        'cart': cart,
    }
    return render(request, 'product/cart.html', context)

# def add_to_cart(request):
#     user= request.user
#     product_id = request.GET.get('prod_id')
#     print(product_id)
#     product = models.Product.objects.get(id=product_id)
    
#     models.Cart.objects.create(user=user, product=product)
#     return redirect('product:cart')

def add_to_cart(request, product_id):
    # Get the product based on the product_id
    user = request.user
    product = get_object_or_404(models.Product, id=product_id)
    
    # # Get the current cart from the session
    # cart = request.session.get('cart', {})

    # # Update the cart with the new product
    # if product_id in cart:
    #     cart[product_id] += 1
    # else:
    #     cart[product_id] = 1

    # # Save the updated cart back to the session
    # request.session['cart'] = cart
    
    Cart.objects.create(user=user, product=product)

    return redirect('product:cart')

def plus_cart(request):
    pass

def minus_cart(request):
    pass

# @login_required(login_url='/account/login/')
def checkout(request):
    return render(request, 'product/checkout.html')