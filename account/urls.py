from django.urls import path
from account.views import login



urlpatterns = [
    path('login/', login, name='login'),
]
