from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=150, verbose_name='Nombre')
    apellidos = models.TextField(max_length=150, verbose_name='Apellidos')
    rut = models.TextField(max_length=10, verbose_name='Rut')