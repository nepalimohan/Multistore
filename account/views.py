from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from product.models import Customer


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
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        username = request.POST['username']
        password = request.POST['pass']
        password2 = request.POST['re_pass']
        
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exists. Please enter another username!!!")
                return redirect('account:register')
            
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email exists. Please enter another email!!!")
                    return redirect('account:register')
                
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, 
                                                        is_active=True)
                    customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name, email=email,
                                                       phone=phone, address=address, city=city)
                    auth.login(request, user)
                    messages.success(request, "User Logged in Successfully!!!")
                    return redirect('home')
        
        print(username)
        return HttpResponse("Register view working")
    return render(request, 'account/register.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You logged out. Login again!!!")
    return redirect('account:login')