from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Caja.models import Producto
from .form import ProductoForm,EditarProductoForm
from django.shortcuts import redirect

@login_required(login_url="/login/")
def Itinerario(request):
    Productos = Producto.objects.all()
    if request.method == 'GET':
        query = request.GET.get('q')
        categoria = request.GET.get('categoria')
        opcion=request.GET.get("consulta")
        if opcion=="0":
            if categoria!="---":
                try:
                    producto=Producto.objects.get(nombre=categoria)
                    producto_db = Producto.objects.get(pk=producto.pk)
                    return render(request,'Itinerario.html',{"Productos":Productos,"producto_db":producto_db})
                except:
                    return render(request,'Itinerario.html',{"Productos":Productos})
            elif query!="":
                try:
                    producto=Producto.objects.get(isbn=query)
                    producto_db = Producto.objects.get(pk=producto.pk)
                    return render(request,'Itinerario.html',{"Productos":Productos,"producto_db":producto_db})
                except:
                    return render(request,'Itinerario.html',{"Productos":Productos})
        if opcion=="1":
            return redirect('/NuevoProducto/')
    return render(request,'Itinerario.html',{"Productos":Productos})

@login_required(login_url="/login/")
def NuevoProducto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/itinerario/')
    else:
        formulario = ProductoForm()
    return render(request, 'NuevoProducto.html', {'formulario': formulario})

@login_required(login_url="/login/")
def EditarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        formulario = EditarProductoForm(request.POST, instance=producto)
        if formulario.is_valid(): 
            formulario.save()
            return redirect('/itinerario/')
    else:
        formulario = EditarProductoForm(instance=producto)
    return render(request, 'EditarProducto.html', {'formulario': formulario})
