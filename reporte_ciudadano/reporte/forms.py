from django.forms import ModelForm
from .models import Usuario, Reporte


class RegistroForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'correo_electronico', 'numero_celular', 'contraseña']
    
class ReporteForm(ModelForm):
    class Meta:
        model = Reporte
        fields = ['tipo_incidencia', 'descripcion', 'direccion', 'imagen']   