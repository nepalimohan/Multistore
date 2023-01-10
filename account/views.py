from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('product:checkout')
        else:
            return redirect('account:login')
        
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You logged out. Login again!!!")
    return redirect('account:login')