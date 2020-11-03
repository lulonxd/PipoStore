from django.db import models
from django import forms
# Create your models here.



class Marca(models.Model):
    nombre      = models.TextField(max_length=100)
    activo      = models.BooleanField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre      =models.TextField(max_length=100)
    activo      =models.BooleanField()
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    marca           = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.SET_NULL)
    categoria	    = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    nombre          = models.TextField(max_length=50)
    descripcion     = models.TextField()
    stock           = models.IntegerField(null=True)
    precioCosto     = models.IntegerField()
    precioVenta     = models.IntegerField()
    imagen          = models.ImageField(upload_to='productos',blank=True , null=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre      = models.CharField(max_length=30)
    apellido    = models.CharField(max_length=30)
    direccion   = models.CharField(max_length=50)
    email       = models.EmailField()
    telefono    = models.IntegerField()
