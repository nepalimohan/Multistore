from django.shortcuts import render
from product.models import Category, SubCategory, Product

# Create your views here.
def home(request):
    category = Category.objects.all().distinct()
    subcategory = SubCategory.objects.all().distinct()
    product = Product.objects.all()
    product = {
        'category':category,
        'subcategory':subcategory,
        'product':product,
    }
    return render(request, 'product/home.html', product)