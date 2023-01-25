from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank= True, related_name='children')
    
    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        
    def __str__(self):
        return f'{self.category.name} | {self.name}'   

class Product(models.Model):
    name = models.CharField(max_length=100)
    # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='categories')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField()  
    clothes_size = models.CharField(max_length=100, blank=True, null=True)
    shoe_size = models.PositiveIntegerField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True, null=False)
    
    
    def __str__(self):
        return self.first_name