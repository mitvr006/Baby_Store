from django.http import HttpResponse
from django.shortcuts import render, redirect

def h(request):
    return HttpResponse("hello")

def home(request):
    return render(request, "shoped.html", {'user': request.user})

def akash(request):
    return render(request, "header.html")


  
