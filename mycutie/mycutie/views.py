from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Product ,Category

def h(request):
    return HttpResponse("hello")

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shoped.html', {'categories': categories,'products': products})

def header(request):
    return render(request, "header.html")

