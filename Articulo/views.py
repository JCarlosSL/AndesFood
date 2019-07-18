from django.shortcuts import render, render_to_response
from django.db.models import Q

# Create your views here.
from django.views import generic


from .models import Articulo


"""se encarga de buscar un articulo en la base de datos"""
def BuscarArticulo(request):
    query = request.GET.get('q','')
    resultslist = Articulo.objects.all() #obtiene todo los objetos
    if query : #query = consulta
        qset = ( 
            Q(type__icontains=query) |
            Q(descripcion__icontains = query)
        )
        results = Articulo.objects.filter(qset).distinct() #filtra los datos
    else:
        results = []
    return render_to_response("Articulo/search.html",{
        "results": results,
        "resultslist": resultslist,
        "query": query
    })

def lista_articulos(request):
    articulos = Articulo.objects.order_by('nombre_articulo')
    return render(request, 'Articulo/lista.html', {'articulos':articulos})
