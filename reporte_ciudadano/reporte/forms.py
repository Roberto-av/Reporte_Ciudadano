from django.forms import ModelForm
from .models import Usuario


class RegistroForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'correo_electronico', 'numero_celular', 'contraseña']