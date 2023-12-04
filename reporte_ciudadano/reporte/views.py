from django.shortcuts import render, redirect
from .models import Usuario
from .forms import RegistroForm
from django.db import IntegrityError

# Create your views here.
def inicio(request):
    return render(request,'base.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': RegistroForm})
    else:
        try:
            form = RegistroForm(request.POST)
            form.save()
            return redirect('registro')
        except IntegrityError:
            return render(request, 'registro.html', {
                'form': RegistroForm,
                'error': 'Alguno de los datos no son correctos'
            })
     

    
     
