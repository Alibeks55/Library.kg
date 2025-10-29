from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me_view, name='about_me'),
    path('time_of_day/', views.time_of_day_view, name='time_of_day'),
    path('quotes_of_great_writers/', views.quotes_of_great_writers_view, name='quotes_of_great_writers')
]