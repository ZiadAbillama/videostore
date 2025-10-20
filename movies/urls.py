from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='list'),
    path('add/', views.movie_create, name='create'),
    path('<str:pk>/', views.movie_detail, name='detail'),
    path('<str:pk>/edit/', views.movie_update, name='update'),
    path('<str:pk>/delete/', views.movie_delete, name='delete'),
]