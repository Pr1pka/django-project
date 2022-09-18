from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='generator'),
    path('about/', views.about, name='about'),
    path('password/', views.password, name='password')
]