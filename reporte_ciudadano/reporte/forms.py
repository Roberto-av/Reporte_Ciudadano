from django.forms import ModelForm
from .models import Usuario, Reporte
from django import forms


class RegistroForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'correo_electronico', 'numero_celular', 'contraseña']
    
class ReporteForm(ModelForm):
    class Meta:
        model = Reporte
        fields = ['tipo_incidencia', 'descripcion', 'direccion', 'imagen']   

class EditarReporteForm(forms.Form):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelto', 'Resuelto')
    ]
    
    estatus = forms.ChoiceField(choices=ESTADOS, label='Estatus')
    comentarios = forms.CharField(widget=forms.Textarea, label='Comentario')