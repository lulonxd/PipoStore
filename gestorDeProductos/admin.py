from django.contrib import admin
from .models import *
# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "email", "telefono")
    search_fields=("nombre","apellido", "telefono", "email")

class productoAdmin(admin.ModelAdmin):
    list_display=("marca", "categoria", "nombre", "descripcion", "stock", "precioCosto", "precioVenta", "imagen")
    list_filter=("categoria",)
    search_fields=("marca", "categoria", "nombre", "descripcion", "stock", "precioCosto", "precioVenta")

class marcaAdmin(admin.ModelAdmin):
    list_display=("nombre", "activo")
    list_filter=("activo",)
    search_fields=("marca",)

class categoriaAdmin(admin.ModelAdmin):
    list_display=("nombre", "activo")
    list_filter=("activo",)
    search_fields=("nombre",)
    

admin.site.register(Cliente, clientesAdmin)
admin.site.register(Producto, productoAdmin)
admin.site.register(Marca, marcaAdmin)
admin.site.register(Categoria, categoriaAdmin)