from django.urls import path
from . import views
app_name = 'ModuloCompras'
urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo',views.producto_view,name='producto_view'),
    path('listar',views.producto_list,name='producto_list'),
    path('editar/<id_producto>/',views.producto_edit,name='producto_edit'),
    path('eliminar/<id_producto>/',views.producto_delete,name='producto_delete'),
    path('usuario',views.provehedor_mostrar, name='provehedor'),
]
