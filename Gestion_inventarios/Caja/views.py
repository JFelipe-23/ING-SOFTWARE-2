from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Login.models import Empleado
from .models import Producto,Pedido
from django.contrib import messages

ListaPoductos=[]

@login_required(login_url="/login/")
def Caja(request):
    cedula = request.user.cedula
    if request.method=="POST":
        valor=request.POST.get("name")
        opcion=request.POST.get("consulta")
        if opcion=="1":
            try:
                producto=Producto.objects.get(isbn=valor)
                producto_db = Producto.objects.get(pk=producto.pk)
                nueva_cantidad = producto_db.cantidad - 1
                if nueva_cantidad >= 0:
                    producto_db.cantidad = nueva_cantidad
                    ListaPoductos.append(producto)
                    producto_db.save()
                else:
                    messages.success(request,f"Cantidad insuficiente para el producto {producto.nombre}")
            except:
                messages.success(request,f"Producto {producto.nombre} no encontrado")
        elif opcion=="2":
            try:
                producto=ListaPoductos.pop()
                producto_db = Producto.objects.get(pk=producto.pk)
                nueva_cantidad = producto_db.cantidad + 1
                producto_db.cantidad = nueva_cantidad
                producto_db.save()
            except:
                messages.success(request, 'No hay productos para eliminar')
        elif opcion=="3":
            ListaPoductos.clear()
        elif opcion=="4":
            try:
                vendedor=Empleado.objects.get(cedula=cedula)
                PedidoF=crear_pedido(Total(ListaPoductos),ListaPoductos,vendedor)
                return render(request,'Factura.html',{'ListaPoductos':ListaPoductos,'Total':Total(ListaPoductos),"Fecha":PedidoF.fecha})
            except:
                messages.success(request, 'No hay productos para pagar')
    return render(request,'caja.html',{'cedula': cedula,'ListaPoductos':ListaPoductos,'Total':Total(ListaPoductos)})

def Factura(request):
    return render(request,'Factura.html')

def Total(ListaPoductos)->float:
    Total=0
    for Lista in ListaPoductos:
        Total+=Lista.precio_final
    return Total

def crear_pedido(total_pedido, productos, vendedor):
    pedido = Pedido.objects.create(
        total_pedido=total_pedido,
        vendedor=vendedor
    )

    if isinstance(productos[0], Producto):
        pedido.productos.add(*productos)
    else:
        productos_objetos = Producto.objects.filter(id__in=productos)
        pedido.productos.add(*productos_objetos)

    pedido.save()

    return pedido