from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Proveedor
from Caja.models import Producto
from .form import ProvedorFormulario

@login_required(login_url="/login/")
def Provedores(request):
    Proveedores = Proveedor.objects.all()
    if request.method=="POST":
        valor=request.POST.get("name")
        if valor!="---":
            proveedor = Proveedor.objects.get(nombre=valor)
            productos = Producto.objects.filter(proveedor=proveedor)
            return render(request,'provedor.html',{"Proveedores":Proveedores,"productos":productos})
        else:
            return render(request,'provedor.html',{"Proveedores":Proveedores})
    return render(request,'provedor.html',{"Proveedores":Proveedores})

@login_required(login_url="/login/")
def NuevoProvedor(request):
    formulario = ProvedorFormulario()
    return render(request, 'NuevoProvedor.html', {'formulario': formulario})