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
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    subcategory_choices = (
        ('Jeans','Jeans'),
        ('Shoes','Shoes'),
        ('Socks','Socks'),
        ('Hoddie','Hoodie'),
    )
    name = models.CharField(max_length=50, choices=subcategory_choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    sizes_choices = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large'),
        ('XXL','Extra Extra Large'),
        )
    
    
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=sizes_choices, null=True, blank=True)
    stock = models.PositiveIntegerField()
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
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
    gender = models.CharField(max_length=10, choices=gender_choices)
    
    def __str__(self):
        return self.first_name
    