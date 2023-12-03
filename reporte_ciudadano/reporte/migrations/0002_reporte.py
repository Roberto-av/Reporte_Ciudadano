# Generated by Django 4.2.7 on 2023-12-03 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_incidencia', models.CharField(choices=[('Bache', 'Bache'), ('Problema de alumbrado', 'Problema de alumbrado'), ('Fuga en alcantarilla', 'Fuga en alcantarilla'), ('Reporte de basura', 'Reporte de basura')], max_length=50)),
                ('descripcion', models.TextField()),
                ('estatus', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Resuelto', 'Resuelto')], default='Pendiente', max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.usuario')),
            ],
        ),
    ]
