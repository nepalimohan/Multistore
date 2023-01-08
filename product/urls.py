from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('shop/', views.shop, name='shop'),
]
