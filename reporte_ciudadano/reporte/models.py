from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    numero_celular = models.CharField(max_length=20, null=True, blank=True)
    contraseña = models.CharField(max_length=128, null=True)

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=128, null=True)
    
class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    TIPOS_INCIDENCIA = (
        ('Bache', 'Bache'),
        ('Problema de alumbrado', 'Problema de alumbrado'),
        ('Fuga en alcantarilla', 'Fuga en alcantarilla'),
        ('Reporte de basura', 'Reporte de basura'),
    )
    tipo_incidencia = models.CharField(max_length=50, choices=TIPOS_INCIDENCIA)
    descripcion = models.TextField()
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelto', 'Resuelto'),
    )
    direccion = models.CharField(max_length=100,null=False, blank=False) 
    estatus = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    comentarios = models.TextField(null=True)

    def __str__(self):
        fila = 'Incidencia:: ' + self.tipo_incidencia + ' - ' + 'Descrpcion -' + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()