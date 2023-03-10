from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from .models import Cart
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.views import View

def home(request):
    try:
        category_name = request.GET.get('category').capitalize()
        product = models.Product.objects.filter(subcategory__category__name=category_name)
        
        context = {
            'product':product
        }
        return render(request, 'product/shop.html', context)
        
    except:
        category = models.Category.objects.all()
        subcategory = models.Subcategory.objects.all().distinct()
        product = models.Product.objects.filter(is_featured=True).order_by('-id')[:8]
        recent_products = models.Product.objects.all().order_by('-id')[:8]
        product = {
            'category':category,
            'subcategory':subcategory,
            'product':product,
            'recent_products':recent_products,
            
        }
        return render(request, 'product/home.html', product)
    
    
def product_details(request, pk):
    product = models.Product.objects.get(pk=pk)
    item_in_cart = False
    try:
        item_in_cart = Cart.objects.filter(Q(product=product.pk) & Q(user=request.user)).exists()
    except:
        item_in_cart = False
    related_products = models.Product.objects.filter(subcategory=product.subcategory).exclude(pk=pk)[:8]
    products = models.Product.objects.all()
    context ={
        'related_products':related_products,
        'product':product,
        'products':products,
        'item_in_cart':item_in_cart,
        
    }
    return render(request, 'product/product_details.html', context)

def products(request, id=None):
    if id:
        product = models.Product.objects.filter(subcategory__id=id)
        context = {
            'product': product,
        }
        
        return render(request, 'product/shop.html', context)
    else:
        product = models.Product.objects.all().order_by('-id')
        context = {
            'product': product,
        }
        
        return render(request, 'product/shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        shipping_amount = 100
        total_amount = 0
        #list comprehension to store cart data of authenticated user
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.price)
                amount+= temp_amount
                total_items = len(Cart.objects.filter(user=request.user))
                total_amount = amount + shipping_amount
                context = {'cart': cart,'total_amount':total_amount,'amount':amount, 'total_items':total_items,'shipping_amount':shipping_amount}
            return render(request, 'product/cart.html', context)
        else:
            return HttpResponse('empty cart')

def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id'] #getting info stored in prod_id from myscript.js
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0
        shipping_amount = 100
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_amount = (p.quantity * p.product.price)
            print(temp_amount)
            
            amount+= temp_amount
        
        

        print(amount)
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
            }
        
        # return HttpResponse('hello')
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id'] #getting info stored in prod_id from myscript.js
        print(prod_id)
        try:
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            if c.quantity >0:
                c.quantity-=1
                c.save()
                amount = 0
                shipping_amount = 100
                cart_product = [p for p in Cart.objects.all() if p.user == request.user]
                for p in cart_product:
                    temp_amount = (p.quantity * p.product.price)
                    amount+= temp_amount

                data = {
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount':amount + shipping_amount
                    }
                return JsonResponse(data)
        except:
            return redirect('product:home')

def add_to_cart(request, product_id):
    # Get the product based on the product_id
    user = request.user
    quantity = request.GET.get('quantity')
    product = get_object_or_404(models.Product, id=product_id)
    if quantity is None:
        cart, created = Cart.objects.get_or_create(user=user, product=product)
        print(cart, '*****')
    else:
        cart, created = Cart.objects.get_or_create(user=user, product=product, quantity=quantity)
        print(cart, '#####')
    if not created:
        return HttpResponse('product exists')
    return redirect('product:cart')

def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id'] #getting info stored in prod_id from myscript.js
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        print(c)
        amount = 0
        shipping_amount = 100
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_amount = (p.quantity * p.product.price)
            amount+= temp_amount
        data = {
            'amount':amount,
            'totalamount':amount + shipping_amount,
            'status': 'Deleted successfully'
            }
        return JsonResponse(data)

# @login_required(login_url='/account/login/')
def checkout(request):
    return render(request, 'product/checkout.html')

def contact(request):
    return render(request, 'product/contact.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'product/contact.html')
    
    def post(self, request):
        name =  request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        pass