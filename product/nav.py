from product import models
from django.contrib.auth.models import User

def navbar(request):
    category = models.Category.objects.all()
    subcategory = models.Subcategory.objects.all().distinct()
    product = models.Product.objects.all().last()
    if request.user.is_authenticated:
        len = models.Cart.objects.filter(user=request.user).count()
        context = {
            'category':category,
            'subcategory':subcategory,
            'product':product,
            'len': len,
        }
    else:
        context = {
            'category':category,
            'subcategory':subcategory,
            'product':product,
        }
    
    return context