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
def product_list(request):
    """Display all products."""
    products = Product.objects.all()
    return render(request, 'blog/product_list.html', {'products': products})

def cart_detail(request):
    cart = request.session.get('cart', {})
    products = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        products.append({'product': product, 'quantity': quantity})
        total_price += product.price * quantity
    return render(request, 'blog/cart_detail.html', {'products': products, 'total_price': total_price})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
    request.session['cart'] = cart
    return redirect('cart_detail')

def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        if quantity > 0:
            cart[product_id] = quantity
        else:
            del cart[product_id]
        request.session['cart'] = cart
    return redirect('cart_detail')





