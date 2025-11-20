from django.shortcuts import render
from . import models

from django.views import generic

class AllProductsView(generic.ListView):
    model = models.Product
    template_name = 'LS_Waikiki/all_products.html'
    context_object_name = 'products'


class NewProductsView(generic.ListView):
    model = models.Product
    template_name = 'LS_Waikiki/new_products.html'
    context_object_name = 'new_products'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='#Новинка')
    

class DiscountProductsView(generic.ListView):
    model = models.Product
    template_name = 'LS_Waikiki/discount_products.html'
    context_object_name = 'discount_products'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='#Скидка')


class HitProductsView(generic.ListView):
    model = models.Product
    template_name = 'LS_Waikiki/hit_products.html'
    context_object_name = 'hit_products'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='#Хит')
    

class AutumnProductsView(generic.ListView):
    model = models.Product
    template_name = 'LS_Waikiki/autumn_products.html'
    context_object_name = 'autumn_products'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='#Осенная коллекция')
    

class PremiumProductsView(generic.ListView):
    model = models.Product
    template_name = 'LS_Waikiki/premium_products.html'
    context_object_name = 'premium_products'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='#Премиум')







# def all_productsView(request):
#     if request.method == 'GET':
#         products = models.Product.objects.all()
#         return render(request, 'LS_Waikiki/all_products.html', {'products': products})
    

# def New_ProductsView(request):
#     if request.method == 'GET':
#         new_products = models.Product.objects.filter(tags__name='#Новинка')
#         return render(request, 'LS_Waikiki/new_products.html', {'new_products': new_products})
    

# def Discount_ProductsView(request):
#     if request.method == 'GET':
#         discount_products = models.Product.objects.filter(tags__name='#Скидка')
#         return render(request, 'LS_Waikiki/discount_products.html', {'discount_products': discount_products})
    

# def Hit_ProductsView(request):
#     if request.method == 'GET':
#         hit_products = models.Product.objects.filter(tags__name='#Хит')
#         return render(request, 'LS_Waikiki/hit_products.html', {'hit_products': hit_products})


# def Autumn_ProductsView(request):
#     if request.method == 'GET':
#         autumn_products = models.Product.objects.filter(tags__name='#Осенная коллекция')
#         return render(request, 'LS_Waikiki/autumn_products.html', {'autumn_products': autumn_products})
    

# def Premium_ProductsView(request):
#     if request.method == 'GET':
#         premium_products = models.Product.objects.filter(tags__name='#Премиум')
#         return render(request, 'LS_Waikiki/premium_products.html', {'premium_products': premium_products})
    

    


