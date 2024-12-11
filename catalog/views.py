from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product_name": product.name,
        "product_description": product.description,
        "product_image": product.image,
        "product_category": product.category,
        "product_price": product.price,
        "product_created_at": product.created_at,
        "product_updated_at": product.updated_at
    }
    return render(request, "catalog/product_detail.html", context=context)


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/home.html', context)
