from django.shortcuts import render, get_object_or_404
from . import models

def categoryView(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        context = {
              'categories': categories
         }
    return render(request, 'shop/categories.html', context=context)


def productView(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        context = {
               'products': products
          }
    return render(request, 'shop/products.html', context=context)


def category_product_View(request, id):
    if request.method == 'GET':
        category = get_object_or_404(models.Category, id=id)
        products = models.Product.objects.filter(category = category) 
        context = {
            'category': category,
            'products': products
        } 
    return render(request, 'shop/category_products.html', context=context)