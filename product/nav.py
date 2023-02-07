from product import models

def navbar(request):
    category = models.Category.objects.all()
    subcategory = models.Subcategory.objects.all().distinct()
    product = models.Product.objects.all().last()
    # print(product.)
    context = {
        'category':category,
        'subcategory':subcategory,
        'product':product,
    }
    return context