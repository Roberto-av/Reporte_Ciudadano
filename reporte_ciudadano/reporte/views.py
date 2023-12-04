from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Reporte, Empleado
from .forms import RegistroForm, ReporteForm, EditarReporteForm
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout as django_logout

# Create your views here.
def inicio(request):
    return render(request,'index.html')

def lista_reportes(request):
    if 'usuario_id' not in request.session:
        # La sesión del usuario no está activa
        return redirect('login')
    reportes = Reporte.objects.filter(usuario_id=request.session.get('usuario_id'))
    return render(request, 'lista.html', {'reportes': reportes})

def lista_reportes_empleado(request):
    if 'usuario_id' not in request.session:
        # La sesión del usuario no está activa
        return redirect('login/empleado')
    #Obtener todos los reportes
    reportes = Reporte.objects.all()
    return render(request, 'lista_empleado.html', {'reportes': reportes})

def reporte(request):
    if 'usuario_id' not in request.session:
        # La sesión del usuario no está activa
        return redirect('login')
    if request.method == 'GET':
        return render(request, 'reporte.html', {'form': ReporteForm()})
          
    else:
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            reporte = form.save(commit=False)
            # Obteniendo el ID del usuario desde la sesión
            usuario_id = request.session.get('usuario_id')
            if usuario_id:
                # Asignando el usuario al reporte si el ID está presente en la sesión
                reporte.usuario_id = usuario_id
                reporte.save()
                return redirect('reporte/lista')
            else:
                # Manejar el caso donde no hay un usuario en la sesión
                messages.error(request, 'Usuario no encontrado.')
        else:
            print(form.errors)  # Imprime los errores del formulario en la consola
            messages.error(request, 'Todos los campos deben estar completados.')
        return render(request, 'reporte.html', {'form': form})

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
        print("Aqui toy")
        try:
            print("Aqui toy 2")
            form = RegistroForm(request.POST)
            form.save()
            return redirect('index')
        except:
            print("Aqui toy 3")
            messages.error(request, 'Todos los campos tienen que estar llenados.')
    print("Aqui toy 4")
    return render(request, 'registro.html')
     
def login_empleado(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
        return redirect('index')
    else:
        if request.method == 'POST':
            correo = request.POST['correo']  # Asegúrate de que los campos coincidan con los nombres en tu formulario HTML
            contraseña = request.POST['contraseña']

            # Busca el usuario en tu tabla de Usuarios
            try:
                empleado = Empleado.objects.get(correo=correo, contraseña=contraseña)
            except Empleado.DoesNotExist:
                empleado = None

            if empleado is not None:
                # Autenticación exitosa, puedes hacer lo que necesites aquí, como establecer una sesión
                # Por ejemplo, podrías usar sesiones de Django para mantener al usuario autenticado
                request.session['usuario_id'] = empleado.id_empleado
                return redirect('reporte/lista/admin')
            else:
                # Si el usuario no existe o las credenciales son incorrectas, muestra un mensaje de error
                messages.error(request, 'El correo o la contraseña son incorrectos, Intentelo nuevamente.')

    return render(request, 'login_empleado.html')
    
def editar_reporte(request, id_reporte):
    if 'usuario_id' not in request.session:
        # La sesión del usuario no está activa
        return redirect('login/empleado')

    reporte = get_object_or_404(Reporte, id_reporte=id_reporte)

    if request.method == 'POST':
        form = EditarReporteForm(request.POST)
        if form.is_valid():
            nuevo_estado = form.cleaned_data['estatus']
            nuevo_comentario = form.cleaned_data['comentarios']

            # Actualizar el estado y comentario del reporte
            reporte.estatus = nuevo_estado
            reporte.comentarios = nuevo_comentario
            reporte.save()

            # Redireccionar a la página de detalles del reporte
            return redirect('reporte/lista/admin')
    else:
        form = EditarReporteForm(initial={'estatus': reporte.estatus, 'comentarios': reporte.comentarios})

    return render(request, 'editar_reporte.html', {'form': form, 'reporte': reporte})
