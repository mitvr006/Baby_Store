# views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from .models import Seller, Product, Order
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import make_password, check_password



def seller_home(request):
    return render(request, 'seller/seller_home.html')

def seller_dashboard(request):
    return render(request, 'seller/seller_dashboard.html')


def view_products(request):
    products = Product.objects.all()
    return render(request, 'seller/view_products.html', {'products': products})

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'seller/view_orders.html', {'orders': orders})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()
    return render(request, 'seller/add_product.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'seller/edit_product.html', {'form': form})


def remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('view_products')
    

def seller_header(request):
    return render(request, 'seller/seller_header.html')

# create a seller login view here request method is get and not post
def seller_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        seller = Seller.objects.filter(email=email).first()

        if seller is not None: 
            if check_password(password, seller.password):
                request.session['seller_id'] = seller.id
                messages.success(request, 'Login successful! Welcome to your dashboard.')
                return redirect('seller_home')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'No seller found with the provided email.')        

    return render(request, 'seller/seller_login.html')


def seller_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        store_name = request.POST.get('store_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if password == confirm_password:
            if Seller.objects.filter(email=email).exists():
                messages.error(request, 'An account with this email already exists.')
            else:    
                hash_password = make_password(password)
                seller = Seller.objects.create(
                    username=username,
                    store_name=store_name,
                    phone_number=phone,
                    store_address=address,
                    email=email,
                    password=hash_password
                )

            request.session['seller_id'] = seller.id
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('seller_login')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'seller/seller_register.html')
    

def logout_view(request):
    logout(request)
    return redirect('seller_dashboard')


# @login_required
# def seller_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('add_product')  # Redirect to the same page after successful submission
#     else:
#         form = ProductForm()
    
#     categories = Category.objects.all()  # Fetch all categories for dropdown
#     return render(request, 'seller_dashboard.html', {
#         'form': form,
#         'categories': categories,
#     })   
        
# def delete_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     product.delete()
#     return redirect('seller-dashboard')

# def update_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('seller-dashboard')
#     else:
#         form = ProductForm(instance=product)
    
#     return render(request, 'seller/seller_dashboard.html', {'form': form})





