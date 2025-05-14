from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
# Create your views here.

def home_view(request):
    return render(request , 'invApp/home.html')

def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {
        'form': form,
    }
    return render(request, 'invApp/product_form.html', context)

def product_read_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'invApp/product_list.html', context)

def product_update_view(request, pk):
    product = Product.objects.get(product_id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'invApp/product_form.html', context)

def product_delete_view(request, pk):
    product = Product.objects.get(product_id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    context = {
        'product': product,
    }
    return render(request, 'invApp/product_confirm_delete.html', context)