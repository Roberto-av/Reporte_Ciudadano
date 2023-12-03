from django.contrib import admin
from .models import Usuario, Empleado, Reporte

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Empleado)
admin.site.register(Reporte)
