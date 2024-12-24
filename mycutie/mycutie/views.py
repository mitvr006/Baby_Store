from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Product

def h(request):
    return HttpResponse("hello")

def home(request):
    products = Product.objects.all()
    return render(request, 'shoped.html', {'products': products})

def akash(request):
    return render(request, "header.html")


  
