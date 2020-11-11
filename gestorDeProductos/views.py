from django.shortcuts import render, redirect
from gestorDeProductos.models import Marca, Categoria, Producto
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password  
from django.conf import settings
from django.contrib.auth import authenticate, login, validators
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.

def registro(request):
    mensaje = ""
    response = redirect('/accounts/login/')
    if request.method == "POST":
        usuario	= request.POST["txtUsuario"]
        nombre  = request.POST['txtNombre']
        apellido  = request.POST['txtApellido']
        correo	= request.POST["txtCorreo"]
        clave	= request.POST["txtClave"]
        confirm = request.POST["txtClave2"]
        value = "foo.bar@baz.qux"

        try:
            validate_email(correo)
        except ValidationError as e:
            mensaje = "Porfavor Ingrese un correo válido"
        else:
            User.objects.create(username=usuario,first_name=nombre,last_name=apellido , email=correo, password=make_password(clave))
            mensaje = "Usuario registrado correctamente"
            return response
    return render(request, 'registration/registro.html', {'mensaje':mensaje})	

def plantilla(request):
    return render(request, 'plantillaBase.html', {})

def buscarPorId(modelo, id):
    try:
        item = modelo.objects.get(pk=id)
    except:
        item = {}
    return item



def marca(request):
    mensaje=""
    lista={}
    item={}

    if request.method == "POST":
        idMarca      = int("0" + request.POST["txtId"])
        nombre  = request.POST["txtNombre"].upper()
        activo  = request.POST.get("chkActivo") == "1"

        if 'btnGrabar' in request.POST:
            if nombre == "":
                mensaje = "Porfavor Ingrese Nombre de Marca"
            elif idMarca < 1:
                Marca.objects.create(nombre=nombre, activo=activo)    
            else:
                item = buscarPorId(Marca, idMarca)
                if not isinstance(item, Marca):
                    mensaje = "No se debe ingresar ID"
                else:
                    item.id = idMarca
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    item = {}
                    mensaje= "Datos Guardados Correctamente"
        elif 'btnBuscar' in request.POST:
            if idMarca == "":
                mensaje = "La id debe ser un número"
            else:
                item = buscarPorId(Marca, idMarca)
                if not isinstance(item, Marca):
                    mensaje = "Registro no encontrado"
                    item = {}
        elif 'btnListar' in request.POST:
            lista = Marca.objects.all()
        elif 'btnEliminar' in request.POST:
            item = Marca.objects.get(pk = idMarca)
            if isinstance(item, Marca):
                item.delete()
                mensaje = "Registro eliminado"
                item = {}
        
    
    contexto = {'mensaje':mensaje, 'lista' : lista, 'item':item}
    return render(request, 'producto/marca.html', contexto)

def categoria(request):
    mensaje=""
    lista={}
    item={}
    errores = {}
    if request.method == "POST":
        id      = int("0" + request.POST["txtId"])
        nombre  = request.POST["txtNombre"].upper()
        activo  = request.POST.get("chkActivo") == "1"
        if 'btnGrabar' in request.POST:
            if nombre == "":
                mensaje = "Porfavor Ingrese Nombre de Categoria"
            elif id < 1:
                Categoria.objects.create(nombre=nombre, activo=activo)
            else:
                item = Categoria.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save()
                item = {}
                mensaje= "Datos Guardados Correctamente"
        elif 'btnBuscar' in request.POST:
            item = buscarPorId(Categoria, id)
            if not isinstance(item, Categoria):
                mensaje = "Registro no encontrado"
                item = {}
        
        elif 'btnListar' in request.POST:
            lista = Categoria.objects.all()
        
        elif 'btnEliminar' in request.POST:
            item = Categoria.objects.get(pk = id)

            if isinstance(item, Categoria):
                item.delete()
                mensaje = "Registro eliminado"
                item = {}
    
    contexto = {'mensaje':mensaje, 'lista':lista, 'item':item,'errores': errores}


    return render(request, 'producto/categoria.html', contexto)

def producto(request):
    mensaje = ""
    lista 	= {}
    item 	= {}
    cmbMarca = Marca.objects.all()
    cmbCategoria = Categoria.objects.all()
    errores	= {}
    if request.method == "POST":
            id          = int("0" + request.POST["txtId"])
            idMarca 	= int("0" + request.POST['cmbMarca'])
            idCategoria = int("0" + request.POST['cmbCategoria'])
            nombre 		= request.POST['txtNombre'].upper()
            descripcion = request.POST['txtDescripcion'].upper()
            stock 		= request.POST['txtStock']
            precioCosto = request.POST['txtPrecioCosto']
            precioVenta	= request.POST['txtPrecioVenta']
            if 'btnGrabar' in request.POST: # validar informacion
                if idMarca < 1:
                    mensaje = "Porfavor Seleccione Marca"
                elif idCategoria < 1:
                    mensaje = "Porfavor seleccione Categoria"
                elif nombre == "":
                    mensaje = "Porfavor ingrese Nombre"
                elif descripcion == "":
                    mensaje = "Porfavor ingrese Descripcion"
                elif stock == "":
                    mensaje = "Porfavor ingrese Stock"
                elif precioCosto == "":
                    mensaje = "Porfavor ingrese precio Costo"
                elif precioVenta == "":
                    mensaje = "Porfavor ingrese Precio de Venta"
                elif id < 1:
                    uploaded_file = request.FILES['imagen']
                    fs = FileSystemStorage()
                    marca = Marca.objects.get(pk=idMarca)
                    categoria = Categoria.objects.get(pk=idCategoria)
                    Producto.objects.create(categoria=categoria, marca=marca, nombre=nombre,descripcion=descripcion,stock=int(stock),precioCosto=int(precioCosto),precioVenta=int(precioVenta), imagen=uploaded_file)
                else:
                    item = buscarPorId(Producto, id)
                    if not isinstance(item, Producto):
                        mensaje = "No se debe ingresar ID"
                    else:
                        item.marca = idMarca
                        item.categoria = idCategoria
                        item.nombre = nombre
                        item.descripcion = descripcion
                        item.stock = stock
                        item.precioCosto = precioCosto
                        item.precioVenta = precioVenta
                        uploaded_file = request.FILES['imagen']
                        fs = FileSystemStorage()
                        item.save()
                        mensaje = "La solicitud fue realizada con éxito"
                    item = {}
            elif 'btnListar' in request.POST: # como filtrar con el ORM
                if idCategoria > 0:
                    lista = Producto.objects.filter(categoria_id = buscarPorId(Categoria, idCategoria))
                elif idMarca > 0:
                    lista = Producto.objects.filter(marca_id = buscarPorId(Marca, idMarca))
                elif descripcion != "":
                    lista = Producto.objects.filter(descripcion__contains = descripcion)
                elif nombre != "":
                    lista = Producto.objects.filter(nombre__contains = nombre)
                elif precioCosto != "":
                    lista = Producto.objects.filter(precioCosto__contains = precioCosto)
                elif precioVenta != "":
                    lista = Producto.objects.filter(precioVenta__contains = precioVenta)
                else:
                    lista = Producto.objects.all()
            elif 'btnBuscar' in request.POST:
                item = buscarPorId(Producto, id)
                if not isinstance(item, Producto):
                    mensaje = "Registro no encontrado"
                
            elif 'btnEliminar' in request.POST:
                item = Producto.objects.get(pk = id)

                if isinstance(item, Producto):
                    item.delete()
                    mensaje = "Registro eliminado"
                    item = {}
    context = {'mensaje' : mensaje, 'lista': lista, 'item': item, 'cmbMarca': cmbMarca, 'cmbCategoria': cmbCategoria, 'errores': errores}
    return render(request, 'producto/producto.html', context)

def inicio(request):
    producto = Producto.objects.all()
    if request.method == "POST":
        buscar = request.POST['txtBuscar'].upper()
        producto = Producto.objects.filter(nombre__contains=buscar)
    return render(request, 'index.html',{"productos":producto})

def buscarBase(request):
    producto = Producto.objects.all()
    if request.method == "POST":
        buscar = request.POST['txtBuscar'].upper()
        producto = Producto.objects.filter(nombre__contains= buscar )
    return render(request, 'index.html',{"productos":producto})

def tarjetaAMD(request):
    producto = Producto.objects.filter(nombre__contains="AMD" )
    return render(request, 'producto/tarjetasAMD.html', {'productos':producto})

def tarjetaNVIDIA(request):
    producto = Producto.objects.filter(nombre__contains="NVIDIA" )
    return render(request, 'producto/tarjetasNVIDIA.html', {'productos':producto})

def memoriaRAM(request):
    nombre = 'RAM'
    producto = Producto.objects.filter(descripcion__contains = 'DDR4')
    return render(request, 'producto/RAM.html', {'productos':producto})






