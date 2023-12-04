from django.shortcuts import render, redirect
from .models import Usuario
from .forms import RegistroForm
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout as django_logout

# Create your views here.
def inicio(request):
    return render(request,'index.html')

def reporte(request):
    if 'usuario_id' not in request.session:
        # Redirigir a la página de inicio de sesión
        return redirect('login')
    return render(request,'reporte.html')

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
            return redirect('index')
        else:
            # Si el usuario no existe o las credenciales son incorrectas, muestra un mensaje de error
            messages.error(request, 'El correo o la contraseña son incorrectos, Intentelo nuevamente.')

    return render(request, 'login.html')

def logout(request):
     # Cerrar sesión de Django
    django_logout(request)
    
    # Eliminar cualquier otra información de sesión que hayas creado
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
        
    return redirect('index')


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
     

    
     
