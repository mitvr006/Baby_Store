from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages 
from django.contrib.auth.hashers import make_password  


def signup(request):
    # if request.method == 'GET':
    #     return render(request, 'signup.html')

    if request.method == 'POST':
        print("hhhhhhhhhhhhhhhhhhhhh")
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'signup.html')

        User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password)  
        )

        messages.success(request, "Account created successfully. Please log in.")
        return redirect("login")  

    return render(request, 'blog/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)  
    return redirect('home')  


