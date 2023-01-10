from django.shortcuts import render, redirect

# Create your views here.
def shop(request):
    return render(request, 'product/shop.html')

def checkout(request):
    return render(request, 'product/checkout.html')