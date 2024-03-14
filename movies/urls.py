from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<str:movieId>', views.movieInfo, name='movieInfo'),
    path('search', views.search, name='search'),
]