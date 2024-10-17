from django.shortcuts import render
from django.db import connection
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

ListaPraductos = []
Total = 0

@login_required(login_url="/logIn/")
def Caja(request):
    if request.method == 'POST' and 0 == len(ListaPraductos):
        consulta_seleccionada = request.POST.get('consulta')
        if consulta_seleccionada == '2':
            data = request.POST.get('name')
            try:
                datos = data
                obj = Product.objects.get(codigo=datos)
                ListaPraductos.append({"codigo": obj.codigo,"nombre": obj.nombre,"precio": obj.precio,"descuento": obj.descuento})
            except:
                return render(request,'caja.html',{"ListaPraductos":ListaPraductos,"Total":0})
            Total= ListaPraductos[0]["precio"]
            return render(request,'caja.html',{"ListaPraductos":ListaPraductos,"Total":Total})
    if 0 != len(ListaPraductos) and request.method == 'POST':
        if request.method == 'POST':
            consulta_seleccionada = request.POST.get('consulta')
            if consulta_seleccionada == '1':
                data = request.POST.get('name')
                print(data)
                try:
                    datos = data
                    obj = Product.objects.get(codigo=datos)
                    ListaPraductos.append({"codigo": obj.codigo,"nombre": obj.nombre,"precio": obj.precio,"descuento": obj.descuento})
                except:
                    return render(request,'caja.html',{"ListaPraductos":ListaPraductos,"Total":Total})
            elif consulta_seleccionada == '2':
                ListaPraductos.pop()
            elif consulta_seleccionada == '3':
                data = request.POST.get('name')
            elif consulta_seleccionada == '5':
                ListaPraductos.clear
            
            n=0
            for lista in ListaPraductos:
                if n == 0:
                    Total=lista["precio"]
                    n=n+1
                else:
                    Total = Total + lista["precio"]
                
            if 0==len(ListaPraductos):
                Total=0
            
            print(ListaPraductos)
            return render(request,'caja.html',{"ListaPraductos":ListaPraductos,"Total":Total})
    else:
        return render(request,'caja.html',{"ListaPraductos":ListaPraductos})
