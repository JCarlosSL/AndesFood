from django.urls import path

from . import views


urlpatterns = [
        path('',views.BuscarArticulo,name='Buscar Articulo'),
        path('',views.lista_articulos,name='listar'),
        ]
