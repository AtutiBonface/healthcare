from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('accounts/login' , views.Login, name= "login"), 
    path('accounts/register' , views.Register, name= "register"),
    path('accounts/logout' , views.Logout, name= "logout"),

    
    
    
]
