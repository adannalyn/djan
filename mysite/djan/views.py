from django.shortcuts import render
from .models import Product

# Create your views here.

def djan(request):
	return render(request, "djan/index.html")

def about(request):
	return render(request, "djan/about.html")

def contact(request):
	return render(request, "djan/contact.html")

def services(request):
    return render(request, "djan/services.html")

def products(request):
    products = Product.objects.all()
    return render(request, 'djan/products.html', {'products':products})