from django.urls import path
from . import views

urlpatterns = [
    path('order_list/', views.OrderListView.as_view(), name='order_list'),
    path('add/<int:book_id>/', views.AddOrderView.as_view(), name='add_order'),
    path('update/<int:id>/', views.UpdateOrderView.as_view(), name='update_order'),
    path('delete/<int:id>/', views.DeleteOrderView.as_view(), name='delete_order'),
]