from django.contrib import admin
from product.models import Category, Product, Customer, Subcategory


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Subcategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_filter = ['category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'size', 'stock', 'description', 'is_featured']
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id',]
    