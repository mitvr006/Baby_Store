from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter product description', 'rows': 4}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter product price'}),
            'photo': forms.ClearableFileInput(),
        }
