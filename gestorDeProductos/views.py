from django.shortcuts import render
from gestorDeProductos.models import Marca, Categoria, Producto

# Create your views here.

def plantilla(request):
    return render(request, 'plantillaBase.html', {})

def login(request):
    return render(request, 'login.html', {})

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
    return render(request, 'marca.html', contexto)

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


    return render(request, 'categoria.html', contexto)

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
            imagen      = request.POST['imagen']
            
            if 'btnGrabar' in request.POST: # validar informacion
                if idMarca < 1: # crear nuevo elemento
                    errores['cmbMarca'] = "Falta seleccionar marca"
                else:
                    marca = Marca.objects.get(pk=idMarca)
                    categoria = Categoria.objects.get(pk=idCategoria)
                    Producto.objects.create(categoria=categoria, marca=marca, nombre=nombre,descripcion=descripcion,stock=stock,precioCosto=precioCosto,precioVenta=precioVenta, imagen=imagen)
                
            elif 'btnListar' in request.POST: # como filtrar con el ORM
                lista = Producto.objects.filter(nombre__contains = nombre)
            elif 'btnBuscar' in request.POST:
                item = Producto.objects.get(pk = id)

                if not isinstance(item, Producto):
                    mensaje = "Registro no encontrado"
                    item = {}
            elif 'btnEliminar' in request.POST:
                item = Producto.objects.get(pk = id)

                if isinstance(item, Producto):
                    item.delete()
                    mensaje = "Registro eliminado"
                    item = {}
    context = {'mensaje' : mensaje, 'lista': lista, 'item': item, 'cmbMarca': cmbMarca, 'cmbCategoria': cmbCategoria, 'errores': errores}
    return render(request, 'producto.html', context)

def index(request):
    lista = {}
    productos = Producto.objects.all()
    return render(request, 'index.html', {"productos":productos})


    


