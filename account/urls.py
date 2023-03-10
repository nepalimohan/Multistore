from django.urls import path
from account.views import login, register, logout

app_name = 'account'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
