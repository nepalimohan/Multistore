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
    
class MensSubCategory(models.Model):
    name = models.CharField(max_length=50, choices=[
        ('Jeans','Jeans'),
        ('Shoes','Shoes'),
        ('Socks','Socks'),
        ('Hoddie','Hoodie'),
    ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name = 'Mens SubCategory'
        verbose_name_plural = 'Mens SubCategories'
    def __str__(self):
        return self.name

class WomensSubCategory(models.Model):
    name = models.CharField(max_length=50, choices=[
        ('Jeans','Jeans'),
        ('Shoes','Shoes'),
        ('Socks','Socks'),
        ('Hoddie','Hoodie'),
    ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Womens SubCategory'
        verbose_name_plural = 'Womens SubCategories'
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    subcategory_men = models.ForeignKey(MensSubCategory, on_delete=models.CASCADE, blank=True, null=True)
    subcategory_woemen = models.ForeignKey(WomensSubCategory, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField()
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    SHOE_SIZES = (
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
    )
    
    def save(self, *args, **kwargs):
        if (self.subcategory_men or self.subcategory_men.name == 'Shoes') or (self.subcategory_women or self.subcategory_women.name == 'Shoes'):
            self.size = self.SHOE_SIZES
        else:
            self.size = self.SIZES
        super().save(*args, **kwargs)
        
    size = models.CharField(max_length=2, blank=True)
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