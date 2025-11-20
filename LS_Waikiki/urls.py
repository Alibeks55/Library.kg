from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.AllProductsView.as_view(), name='all_products'),
    path('new_products/', views.NewProductsView.as_view(), name='new_products'),
    path('discount_products/', views.DiscountProductsView.as_view(), name='discount_products'),
    path('hit_products/', views.HitProductsView.as_view(), name='hit_products'),
    path('autumn_products/', views.AutumnProductsView.as_view(), name='autumn_products'),
    path('premium_products/', views.PremiumProductsView.as_view(), name='premium_products')
]