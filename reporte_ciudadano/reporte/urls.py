from django.urls import path
from . import views

urlpatterns = [
     path('', views.inicio, name='inicio'),
     path('login/', views.login, name='login'),
     path('registro/', views.registro, name='registro'),
    # path('/reportes', views.reportes, name='reportes'),
]