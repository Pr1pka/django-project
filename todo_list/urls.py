from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo_home'),
    path('signup/', views.signupuser, name='signupuser'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('create/', views.createtodo, name='createtodo'),
    path('current/<int:todo_pk>/', views.detailtodo, name='detailtodo'),
    path('<int:todo_pk>/complete/', views.completetodo, name='completetodo'),
    path('<int:todo_pk>/delete/', views.deletetodo, name='deletetodo')
]