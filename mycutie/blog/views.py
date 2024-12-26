from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse , JsonResponse
from .models import Product
from .forms import ProductForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages 
from django.contrib.auth.hashers import make_password  
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'blog/signup.html')

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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)  
    return redirect('home') 

#cart code in views.py 
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('product_list')  
    else:
        form = ProductForm()  

    return render(request, 'blog/add_cart.html', {'form': form}) 

def product_list(request):
    products = Product.objects.all()
    print("product", products)
    return render(request, 'shoped.html', {'products': products})


def product_detail(request, product_id):
    product = {
        "id": product_id,
        "name": "Sample Product",
        "price": 199.99,
        "description": "This is a high-quality product perfect for everyday use.",
        "image_url": "product-image.jpg"
    }
    return render(request, 'product_detail.html', {"product": product})










