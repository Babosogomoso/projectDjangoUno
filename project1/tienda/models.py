from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=150, verbose_name='nombre')
    apellidos = models.TextField(max_length=150, verbose_name='apellidos')
    rut = models.TextField(max_length=10, verbose_name='rut')

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    Tipo = models.TextField(max_length=150, verbose_name='Tipo de Servicio')
    Valor = models.IntegerField(max_length=150, verbose_name='Precio')

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombreProducto = models.TextField(max_length=150, verbose_name='Nombre Producto')
    Valor = models.FloatField(max_length=150, verbose_name='Precio')

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(max_length=150, verbose_name='Fecha Reserva')
    Hora = models.TimeField(max_length=150, verbose_name='Hora Reserva')
    direccion = models.TextField(max_length=150, verbose_name='Direccion')
    telefono = models.IntegerField(max_length=150, verbose_name='Telefono')
    observacion = models.TextField(max_length=150, verbose_name='Obervacion')
    Valor = models.FloatField(max_length=150, verbose_name='Valor reserva')

