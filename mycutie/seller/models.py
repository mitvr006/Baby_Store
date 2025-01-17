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
class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField( blank=True, null=True)
    category = models.CharField(max_length=100 , blank=True, null=True)
    image = models.ImageField(upload_to='products/' , blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']

    

