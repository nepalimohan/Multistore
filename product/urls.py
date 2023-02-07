from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('product/<int:id>', views.products, name='product'),
    path('shop/<int:id>', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    path('pluscart/', views.plus_cart, name='plus_cart'),
    
]
