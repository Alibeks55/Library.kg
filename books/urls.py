from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.AboutMeView.as_view(), name='about_me'),
    path('time_of_day/', views.TimeOfDayView.as_view(), name='time_of_day'),
    path('quotes_of_great_writers/', views.QuotesOfGreatWritersView.as_view(), name='quotes_of_great_writers'),

    path('', views.BooksListView.as_view(), name='book_list'),
    path('book_list/<int:id>/', views.BooksDetailView.as_view(), name='book_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]
