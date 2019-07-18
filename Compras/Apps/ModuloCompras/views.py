from django.shortcuts import render,redirect
from django.http import HttpResponse
from Apps.ModuloCompras.forms import ProductoForm,ProvehedorForm
from Apps.ModuloCompras.models import Producto,Producto_Almacen,Compra,Compra_Producto,Provehedor

# Create your views here.
def index(request):
    return render(request,'ModuloCompras/index.html')
# Create your views here.
def producto_view(request):
    if request.method=='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ModuloCompras:index')
    else:
        form=ProductoForm()
    return render(request,'ModuloCompras/productoForm.html',{'form':form})    
def producto_list(request):
    producto=Producto.objects.all().order_by('id')
    contexto={'productos':producto}
    return render(request,'ModuloCompras/productoLista.html',contexto)
def producto_edit(request,id_producto):
    producto=Producto.objects.get(id=id_producto)
    if request.method== 'GET':
        form=ProductoForm(instance=producto)
    else:
        form=ProductoForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
        return redirect('ModuloCompras:producto_list')
    return render(request,'ModuloCompras/productoForm.html',{'form':form})    
def producto_delete(request,id_producto):
    producto=Producto.objects.get(id=id_producto)
    if request.method== 'POST':
        producto.delete()
        return redirect('ModuloCompras:producto_list')
    return render(request,'ModuloCompras/productoDelete.html',{'producto':producto})    
def provehedor_mostrar(request):
    provehedor=Provehedor.objects.all()
    contexto={'provehedores':provehedor}
    return render(request,'ModuloCompras/index.html',contexto)
