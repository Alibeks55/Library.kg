from django.urls import path
from . import views

app_name = 'it_users'

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.authloginView, name='login'),
    path('logout/', views.authLogoutView, name='logout'),
    path('user_list/', views.it_user_list_view, name='user_list'),
]