from django.urls import path
from . import views

urlpatterns = [
    path('order_list/', views.order_List_View, name='order_list'),
    path('add/<int:book_id>/', views.add_order, name='add_order'),
    path('update/<int:id>/', views.update_order, name='update_order'),
    path('delete/<int:id>/', views.delete_order, name='delete_order'),
]