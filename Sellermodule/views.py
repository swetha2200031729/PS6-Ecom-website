<<<<<<< HEAD
# views.py in your app
from django.shortcuts import render

def home(request):
    # Logic for the home page
    return render(request, 'home.html')

def login(request):
    # Logic for the login page
    return render(request, 'login.html')

def register(request):
    # Logic for the register page
    return render(request, 'register.html')

def collection(request):
    # Logic for the register page
    return render(request, 'collection.html')
def sales(request):
    # Logic for the register page
    return render(request, 'sales.html')

def cart(request):
    # Logic for the register page
    return render(request, 'cart.html')

def profile(request):
    # Logic for the register page
    return render(request, 'profile.html')
=======
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        username = request.POST.get('nm')
        password = request.POST.get('pwd')
        user = authenticate(request,username = username,password = password )
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return redirect("login")

    return render(request,'login.html')

def logout(request):
    logout("request")
    return redirect('login')
>>>>>>> 0e6f707d86d6c97ff38dd31439e3c8f8e166464b

