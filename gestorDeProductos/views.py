from django.shortcuts import render, redirect
from gestorDeProductos.models import Marca, Categoria, Producto
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def plantilla(request):
    return render(request, 'plantillaBase.html', {})

def buscarPorId(modelo, id):
	try:
		item = modelo.objects.get(pk=id)
	except:
		item = {}
	return item

def resetPassword(request):
    return render(request, 'password_change_form.html', {})

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form':form})

def marca(request):
    mensaje=""
    lista={}
    item={}

    if request.method == "POST":
        id      = int("0" + request.POST["txtId"])
        nombre  = request.POST["txtNombre"]
        activo  = request.POST.get("chkActivo") is "1"

        if 'btnGrabar' in request.POST:
            if id < 1:
                Marca.objects.create(nombre=nombre, activo=activo)
                
            else:
                item = Marca.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save()
                item = {}
            mensaje= "Datos Guardados Correctamente"
        elif 'btnBuscar' in request.POST:
            item = Marca.objects.get(pk = id)

            if not isinstance(item, Marca):
                mensaje = "Registro no encontrado"
                item = {}
        
        elif 'btnListar' in request.POST:
            lista = Marca.objects.all()
        
        elif 'btnEliminar' in request.POST:
            item = Marca.objects.get(pk = id)

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

    if request.method == "POST":
        id      = int("0" + request.POST["txtId"])
        nombre  = request.POST["txtNombre"]
        activo  = request.POST.get("chkActivo") is "1"

        if 'btnGrabar' in request.POST:
            if id < 1:
                Categoria.objects.create(nombre=nombre, activo=activo)
                
            else:
                item = Categoria.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save()
                item = {}
            mensaje= "Datos Guardados Correctamente"
        elif 'btnBuscar' in request.POST:
            item = Categoria.objects.get(pk = id)

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
    
    contexto = {'mensaje':mensaje, 'lista':lista, 'item':item}


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
            nombre 		= request.POST['txtNombre']
            descripcion = request.POST['txtDescripcion']
            stock 		= int("0" + request.POST['txtStock'])
            precioCosto = int("0" + request.POST['txtPrecioCosto'])
            precioVenta	= int("0" + request.POST['txtPrecioVenta'])
            
            if 'btnGrabar' in request.POST: # validar informacion
                if idMarca < 1 or idCategoria < 1: # crear nuevo elemento
                    errores['cmbMarca'] = "Falta seleccionar marca"
                elif id < 1:
                    uploaded_file = request.FILES['imagen']
                    fs = FileSystemStorage()
                    marca = Marca.objects.get(pk=idMarca)
                    categoria = Categoria.objects.get(pk=idCategoria)
                    Producto.objects.create(categoria=categoria, marca=marca, nombre=nombre,descripcion=descripcion,stock=stock,precioCosto=precioCosto,precioVenta=precioVenta, imagen=uploaded_file)
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
                lista = Producto.objects.filter(nombre__contains = nombre)
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
    lista = {}
    productos = Producto.objects.all()
    return render(request, 'index.html', {"productos":productos})




