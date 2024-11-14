from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Proveedor
from Caja.models import Producto
from .form import ProvedorFormulario , EditarProvedorFormulario
from django.shortcuts import redirect

@login_required(login_url="/login/")
def Provedores(request):
    Proveedores = Proveedor.objects.all()
    if request.method=="POST":
        valor=request.POST.get("name")
        proveedor = Proveedor.objects.get(nombre=valor)
        if valor!="---":
            productos = Producto.objects.filter(proveedor=proveedor)
            print(proveedor.pk)
            return render(request,'provedor.html',{"Proveedores":Proveedores,"productos":productos,"proveedor":proveedor})
        else:
            return render(request,'provedor.html',{"Proveedores":Proveedores,"proveedor":proveedor})
    return render(request,'provedor.html',{"Proveedores":Proveedores})

@login_required(login_url="/login/")
def NuevoProvedor(request):
    formulario = ProvedorFormulario()
    return render(request, 'NuevoProvedor.html', {'formulario': formulario})

@login_required(login_url="/login/")
def EditarProvedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        formulario = EditarProvedorFormulario(request.POST, instance=proveedor)
        if formulario.is_valid(): 
            formulario.save()
            return redirect('/itinerario/')
    else:
        formulario = EditarProvedorFormulario(instance=proveedor)
    return render(request, 'EditarProveedor.html', {'formulario': formulario})