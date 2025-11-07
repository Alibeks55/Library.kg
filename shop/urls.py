from django.urls import path
from . import views

urlpatterns = [
    path('category_list/', views.categoryView, name='category_list'),
    path('product_list/', views.productView, name='product_list'),
    path('category_list/<int:id>/', views.category_product_View, name='category_product'),
]