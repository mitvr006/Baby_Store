# views.py
from django.shortcuts import render, redirect
from .serializers import ProductForm
from django.contrib.auth.decorators import login_required
from .models import Seller
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import make_password, check_password

def seller_dashboard(request):
    seller_id = request.session.get('seller_id')
    if seller_id:
        seller = Seller.objects.get(id=seller_id)
        return render(request, 'seller/seller_dashboard.html', {'seller': seller})
    return render(request, 'seller/seller_dashboard.html')

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
                return redirect('seller_dashboard')
            else:
                messages.error(request, 'Invalid email or password.')

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
            return redirect('seller_login')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'seller/seller_register.html')
    

def logout_view(request):
    logout(request)
    return redirect('seller_dashboard')


@login_required
def seller_product(request):
    try:
        seller = Seller.objects.get(user=request.user)
    except Seller.DoesNotExist:
        return redirect('seller_product')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = seller
            product.save()
            return redirect('seller_dashboard')
    else:
        form = ProductForm()

    return render(request, 'seller/seller_product.html', {'form': form})
