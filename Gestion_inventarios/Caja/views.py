from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Login.models import Empleado
from .models import Producto,Pedido
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template

ListaPoductos=[]

@login_required(login_url="/login/")
def Caja(request):
    Productos = Producto.objects.all()
    cedula = request.user.cedula
    if request.method=="POST":
        valor=request.POST.get("name")
        opcion=request.POST.get("consulta")
        if opcion=="1":
            try:
                producto=Producto.objects.get(nombre=valor)
                producto_db = Producto.objects.get(pk=producto.pk)
                nueva_cantidad = producto_db.cantidad - 1
                if nueva_cantidad >= 0:
                    producto_db.cantidad = nueva_cantidad
                    ListaPoductos.append(producto)
                    producto_db.save()
                else:
                    messages.success(request,f"Cantidad insuficiente para el producto {producto.nombre}")
            except:
                messages.success(request, 'No hay este productos')
        elif opcion=="2":
            pocicion=BuquedaEnLista(ListaPoductos,valor)
            if pocicion!=None:
                producto=ListaPoductos.pop(pocicion)
                producto_db = Producto.objects.get(pk=producto.pk)
                nueva_cantidad = producto_db.cantidad + 1
                producto_db.cantidad = nueva_cantidad    
                producto_db.save()
            else:
                messages.success(request, 'No hay productos para eliminar')
        elif opcion=="3":
            recargar(ListaPoductos)
        elif opcion=="4":
            if ListaPoductos!=[]:
                try:
                    vendedor=Empleado.objects.get(cedula=cedula)
                    PedidoF=crear_pedido(Total(ListaPoductos),ListaPoductos,vendedor)
                    ListaCopia=limpiar(ListaPoductos)
                    template = get_template('Factura.html')
                    contexto={'ListaPoductos':ListaCopia,'Total':Total(ListaCopia),"Fecha":PedidoF.fecha,"Productos":Productos}
                    html = template.render(contexto)
                    response = HttpResponse(html)
                    response['Content-Disposition'] = 'attachment; filename="Factura.html"'
                    return response
                except:
                    messages.success(request, 'No hay productos para pagar')
    return render(request,'caja.html',{'cedula': cedula,'ListaPoductos':ListaPoductos,'Total':Total(ListaPoductos),"Productos":Productos})

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

def BuquedaEnLista(ListaPoductos:list,nombre:str)->int:
    contador=0
    for lista in ListaPoductos:
        if lista.nombre==nombre:
            return contador
        else:
            contador=contador+1

def recargar(ListaPoductos:list)->None:
    for lista in ListaPoductos:
        producto_db = Producto.objects.get(pk=lista.pk)
        nueva_cantidad = producto_db.cantidad + 1
        producto_db.cantidad = nueva_cantidad    
        producto_db.save()
    ListaPoductos.clear()

def limpiar(ListaPoductos:list)->list:
    ListaCopia=[]
    for lista in ListaPoductos:
        ListaCopia.append(lista)
    ListaPoductos.clear()
    return ListaCopia