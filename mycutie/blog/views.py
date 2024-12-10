from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse , JsonResponse
from .models import Product
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
def product_list(request):
    """Display all products."""
    products = Product.objects.all()
    return render(request, 'blog/product_list.html', {'products': products})

def cart_detail(request):
    """Display the cart."""
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'blog/cart_detail.html', {'cart': cart, 'total': total})

def add_to_cart(request, product_id):
    """Add an item to the cart."""
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }

    request.session['cart'] = cart
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    """Remove an item from the cart."""
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart_detail')






