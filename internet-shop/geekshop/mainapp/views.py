import random

from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Product, ProductCategory


def index(reqest):
    products = Product.objects.all()[:4]
    return render(
        reqest,
        "mainapp/index.html",
        context={
            "current_year": timezone.now().year,
            "title": "Главная",
            "products": products,
        },
    )


def get_hot_product(queryset):
    return random.choice(queryset)


def products(reqest):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    hot_product = get_hot_product(products)
    return render(
        reqest,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "products": products.exclude(pk=hot_product.pk)[:4],
            "categories": categories,
            "hot_product": hot_product,
        },
    )


def category(reqest, category_id, page=1):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=category_id)
    products = Product.objects.filter(category=category)

    paginator = Paginator(products, 3)
    try:
        products_page = paginator.page(page)
    except:
        products_page = paginator.page(paginator.num_pages)

    return render(
        reqest,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "products": products_page,
            "paginator": paginator,
            "page": products_page,
            "categories": categories,
            "category": category,
            "hot_product": get_hot_product(products),
        },
    )


def product(reqest, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = ProductCategory.objects.all()
    return render(
        reqest,
        "mainapp/product.html",
        context={
            "title": "Продукты",
            "product": product,
            "categories": categories,
        },
    )


def contact(reqest):
    return render(
        reqest,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
        },
    )
