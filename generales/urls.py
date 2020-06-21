from django.urls import path

from .views import (index, 
                    MaterialesCreate, 
                    CategoriaCreate, 
                    ProductoCreate,
                    MaterialesList,
                    CategoriaList,
                    ProductoList,
                    MaterialDetail,
                    CategoriaDetail,
                    ProductoDetail,
                    MaterialesUpdate,
                    CategoriaUpdate,
                    ProductoUpdate)

urlpatterns = [
    path('', index, name="index"),
    path('materiales/', MaterialesCreate.as_view(), name="MaterialesCreate"),
    path('categorias/', CategoriaCreate.as_view(), name="CategoriaCreate"),
    path('producto/', ProductoCreate.as_view(), name="ProductoCreate"),
    #detalle
    path('materiales/<int:pk>', MaterialDetail.as_view(), name="MaterialesDetail"),
    path('categorias/<int:pk>', CategoriaDetail.as_view(), name="CategoriasDetail"),
    path('producto/<int:pk>', ProductoList.as_view(), name="ProductoDetail"),
    #Listado
    path('materiales/listar/', MaterialesList.as_view(), name="MaterialesList"),
    path('categorias/listar/', CategoriaList.as_view(), name="CategoriasList"),
    path('producto/listar/', ProductoList.as_view(), name="ProductoList"),
    #Actualización
    path('materiales/update/<int:pk>', MaterialesUpdate.as_view(), name="MaterialesUpdate"),
    path('categorias/update/<int:pk>', CategoriaUpdate.as_view(), name="CategoriasUpdate"),
    path('producto/update/<int:pk>', ProductoUpdate.as_view(), name="ProductoUpdate"),   
]