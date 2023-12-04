from django.urls import path
from . import views

urlpatterns = [
     path('inicio', views.inicio, name='index'),
     path('login/', views.login, name='login'),
     path('registro/', views.registro, name='registro'),
     path('reporte', views.reporte, name='reporte'),
     path('logout', views.logout, name='logout'),
]