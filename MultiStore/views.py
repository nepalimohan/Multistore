from django.shortcuts import render
from product import models

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