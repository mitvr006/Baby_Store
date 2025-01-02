from django.contrib import admin
from .models import Category,Product

# Register your models here.
admin.site.register(Category)

class Productadmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category') 
admin.site.register(Product, Productadmin)