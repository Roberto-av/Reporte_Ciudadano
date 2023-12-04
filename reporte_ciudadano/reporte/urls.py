from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
     path('', views.inicio, name='index'),
     path('login/', views.login, name='login'),
     path('registro/', views.registro, name='registro'),
     path('reporte', views.reporte, name='reporte'),
     path('logout', views.logout, name='logout'),
     path('reporte/lista', views.lista_reportes, name='lista-reporte'),
     path('login/empleado', views.login_empleado, name='login/empleado'),
     path('reporte/lista/admin', views.lista_reportes_empleado, name='reporte/lista/admin'),
     path('reporte/lista/admin/editar/<int:id_reporte>/', views.editar_reporte, name='reporte/lista/admin/editar'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)