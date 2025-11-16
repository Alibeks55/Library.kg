from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_productsView, name='all_products'),
    path('new_products/', views.New_ProductsView, name='new_products'),
    path('discount_products/', views.Discount_ProductsView, name='discount_products'),
    path('hit_products/', views.Hit_ProductsView, name='hit_products'),
    path('autumn_products/', views.Autumn_ProductsView, name='autumn_products'),
    path('premium_products/', views.Premium_ProductsView, name='premium_products')
]