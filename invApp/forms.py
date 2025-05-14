from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Product Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'e.g. 1'}),
            'name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'e.g. Shirt'}),
            'sku': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'e.g. 12345'}),
            'price': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'e.g. 19.99'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'e.g. 100'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'e.g. Supplier Name'}),
        }

