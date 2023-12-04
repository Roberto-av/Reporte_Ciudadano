from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
     path('inicio', views.inicio, name='index'),
     path('login/', views.login, name='login'),
     path('registro/', views.registro, name='registro'),
     path('reporte', views.reporte, name='reporte'),
     path('logout', views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)