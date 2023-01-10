from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You logged out. Login again!!!")
    return redirect('account:login')