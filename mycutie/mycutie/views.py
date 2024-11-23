from django.http import HttpResponse
from django.shortcuts import render

def h(request):
    return HttpResponse("hello")

def home(request):
    return render(request, "shoped.html")

def akash(request):
    return render(request, "header.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")    
