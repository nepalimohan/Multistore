from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('product/<int:id>', views.products, name='product'),
    path('shop/', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
]
