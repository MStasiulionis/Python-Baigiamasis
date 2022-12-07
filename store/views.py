import datetime
from decimal import Decimal

from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product_all(request):
    products = Product.products.filter(is_active=True, in_stock=True)
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    if product.valid_to < (datetime.date.today() + datetime.timedelta(days=7)):
        product.price = round((product.price * Decimal(0.8)), 2)
        return render(request, 'store/products/single.html', {'product': product})
    else:
        return render(request, 'store/products/single.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
