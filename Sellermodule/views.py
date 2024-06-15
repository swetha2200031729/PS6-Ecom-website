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

