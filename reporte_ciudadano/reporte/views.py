from django.shortcuts import render, redirect
from .models import Usuario
from .forms import RegistroForm
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'base.html')

def login(request):
    if request.method == 'POST':
        correo = request.POST['correo_electronico']  # Asegúrate de que los campos coincidan con los nombres en tu formulario HTML
        contraseña = request.POST['contraseña']

        # Busca el usuario en tu tabla de Usuarios
        try:
            usuario = Usuario.objects.get(correo_electronico=correo, contraseña=contraseña)
        except Usuario.DoesNotExist:
            usuario = None

        if usuario is not None:
            # Autenticación exitosa, puedes hacer lo que necesites aquí, como establecer una sesión
            # Por ejemplo, podrías usar sesiones de Django para mantener al usuario autenticado
            request.session['usuario_id'] = usuario.id_usuario
            return redirect('registro')
        else:
            # Si el usuario no existe o las credenciales son incorrectas, muestra un mensaje de error
            messages.error(request, 'El correo o la contraseña son incorrectos, Intentelo nuevamente.')

    return render(request, 'login.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': RegistroForm})
    else:
        try:
            form = RegistroForm(request.POST)
            form.save()
            return redirect('registro')
        except:
            messages.error(request, 'Todos los campos tienen que estar llenados.')

    return render(request, 'registro.html')
     

    
     
