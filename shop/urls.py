from django.urls import path
from . import views

urlpatterns = [
    path('category_list/', views.CategoryView.as_view(), name='category_list'),
    path('product_list/', views.ProductView.as_view(), name='product_list'),
    path('category_list/<int:id>/', views.CategoryProductView.as_view(), name='category_product'),
]