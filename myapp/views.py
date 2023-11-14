from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your views here.
# from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
User = get_user_model()
def home(request):
    return render(request, 'index.html')

def Login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']  
        
        user = authenticate(request, email=email, password=password) 
        
        if user is not None: 
            login(request, user)  
            return redirect('home') 

        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login') 

   

            
    
    return render(request, 'login.html')
def Logout(request):
    logout(request)
    return redirect('home')

def Register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        
        if password != password2:
            messages.info(request, 'Password does not match!')
            redirect('register')
        else:    
            user = User.objects.create_user(email,username, password)
            user.save()
            return redirect('login')
    return render(request, 'register.html')