from django.urls import path, include

from .views import (index, 
                    MaterialesCreate, 
                    CategoriaCreate, 
                    ProductoCreate)

urlpatterns = [
    path('', index, name="index"),
    path('materiales/', MaterialesCreate.as_view(), name="MaterialesForm"),
    path('categorias/', CategoriaCreate.as_view(), name="CategoriaCreate"),
    path('producto/', ProductoCreate.as_view(), name="ProductoCreate"),
]
