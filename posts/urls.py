from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.index, name='index'),
    path('about/', views.about, name='about'),
]
