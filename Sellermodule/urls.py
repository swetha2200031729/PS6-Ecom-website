from django.urls import path
from . import views
from .views import login_user

urlpatterns = [
    path('',login_user ,name = "login" ),
    # Define other URL patterns here
]
