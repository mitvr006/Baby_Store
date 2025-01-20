from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity', 'description', 'price', 'gender', 'photos', 'seller']
        widgets = {
            'gender': forms.Select(attrs={'placeholder': 'Select product gender'}),
            
        }
