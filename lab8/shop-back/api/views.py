from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()

    category_id = request.GET.get("category")
    is_active = request.GET.get("is_active")
    search = request.GET.get("search")

    if category_id:
        products = products.filter(category_id=category_id)

    if is_active:
        is_active = is_active == "true"
        products = products.filter(is_active=is_active)

    if search:
        products = products.filter(name__icontains=search)

    data = []
    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "count": product.count,
            "is_active": product.is_active,
            "category": product.category.__str__()
        })

    return JsonResponse(data, safe=False)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return JsonResponse({
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description
    })

def category_list(request):
    categories = Category.objects.all()
    data = [
        {
            "id": c.id,
            "name": c.name
        } for c in categories
    ]
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    return JsonResponse({
        "id": category.id,
        "name": category.name
    })

def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    data = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price
        } for p in products
    ]
    return JsonResponse(data, safe=False)
