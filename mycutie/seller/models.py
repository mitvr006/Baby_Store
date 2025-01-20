# models.py
from django.db import models
from django.contrib.auth.models import User
    
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=True, null=True)
    store_name = models.CharField(max_length=100 , blank=True, null=True)
    store_address = models.TextField( blank=True, null=True)
    phone_number = models.CharField(max_length=15 , blank=True, null=True)
    email = models.EmailField( blank=True, null=True)
    store_image = models.ImageField(upload_to='store_images/', blank=True, null=True)
    password = models.CharField(max_length=100 , blank=True, null=True)
    username = models.CharField(max_length=100 , blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    

    def __str__(self):
        return self.store_name
    
# the add the product model 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # Add this field
    name = models.CharField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=[('B', 'Boy'), ('G', 'Girl')], default='U', blank=True, null=True)
    photos = models.ImageField(upload_to="product_photos/", blank=True, null=True, default=None)    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

        

    

