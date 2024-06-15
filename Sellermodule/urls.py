from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('collection/', views.login, name='collection'),
    path('sales/', views.register, name='sales'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),


=======
from .views import login_user

urlpatterns = [
    path('',login_user ,name = "login" ),
    # Define other URL patterns here
>>>>>>> 0e6f707d86d6c97ff38dd31439e3c8f8e166464b
]
