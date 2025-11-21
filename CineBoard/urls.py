from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmListView.as_view(), name='cine_film_list'),
    path('film_detail/<int:id>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('film_create/', views.FilmCreateView.as_view(), name='film_create'),
    path('film_update/<int:id>/', views.FilmUpdateView.as_view(), name='film_update'),
    path('film_delete/<int:id>/', views.FilmDeleteView.as_view(), name='film_delete'),
    path('search/', views.SearchView.as_view(), name='cine_search'),

    path('register/', views.RegisterView.as_view(), name='cine_register'),
    path('login/', views.AuthLoginView.as_view(), name='cine_login'),
    path('logout/', views.AuthLogoutView.as_view(), name='cine_logout'),
]