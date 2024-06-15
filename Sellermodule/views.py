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

