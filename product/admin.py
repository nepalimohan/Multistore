from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from product.models import Category, Product, Customer, Subcategory
from django.contrib.auth.models import Group, User

# admin.site.unregister(Group)
# admin.site.unregister(User)

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'parent')
    icon_name = 'reorder'


@register(Subcategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    icon_name = 'view_comfy'

@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'description', 'is_featured')
    icon_name = 'photo'
    
@register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ('id',)
    icon_name = 'person'
    


# Register your models here.
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']


# @admin.register(Subcategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'category']
#     list_filter = ['category']


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'price', 'size', 'stock', 'description', 'is_featured']
    
# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['id',]
    