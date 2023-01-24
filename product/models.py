from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_choices = (
        ('Mens','Mens'),
        ('Womens','Womens'),
        ('Unisex','Unisex'),
    )
    name = models.CharField(max_length=50, choices=category_choices)

    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank= True, related_name='children')
    
    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=50, choices=[
        ('Jeans','Jeans'),
        ('Shoes','Shoes'),
        ('Socks','Socks'),
        ('Hoddie','Hoodie'),
    ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        
    def __str__(self):
        return f'{self.category.name} | {self.name}'   

class Product(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField()
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
    )
    SHOE_SIZES = (
        (39, 39),
        (40, 40),
        (41, 41),
        (42, 42),
        (42, 42),
    )    
    clothes_size = models.CharField(max_length=3, choices=SIZES ,blank=True, null=True)
    shoe_size = models.PositiveIntegerField(choices=SHOE_SIZES ,blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    city_choices = (
        ('Kathmandu','Kathmandu'),
        ('Chitwan','Chitwan'),
        ('Pokhara','Pokhara'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50,choices=city_choices)
    
    
    def __str__(self):
        return self.first_name