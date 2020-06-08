from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext

from django.views.generic import CreateView, ListView, DetailView

from .precios import CalcularPrecios

from .forms import (MaterialesCreateForm,
                    CategoriaCreateForm,
                    ProductoCreateForm)

def index(request):
    fn, ml, mp = CalcularPrecios()
    titulos = ['Producto','1-99','100-249','250-499','500-999','1000+']
    return render(request, 'precios.html', {'fn':fn, 
                                          'ml': ml,
                                          'mp': mp,
                                          'titulos':titulos})


# ========  MATERIALES ============

class MaterialesCreate(CreateView):
    form_class = MaterialesCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        instance = super(MaterialesCreate, self).get_context_data(**kwargs)
        instance['nombre_cabecera'] = 'Materiales'
        instance['nombre_fomulario'] = 'Formulario para Crear Materiales'
        return instance


# =========== CATEGORIA =============

class CategoriaCreate(CreateView):
    form_class = CategoriaCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        instance = super(CategoriaCreate, self).get_context_data(**kwargs)
        instance['nombre_cabecera'] = 'Categoria'
        instance['nombre_fomulario'] = 'Formulario para Crear Categorias'
        return instance

# ============= PRODUCTO =============

class ProductoCreate(CreateView):
    form_class = ProductoCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        instance = super(ProductoCreate, self).get_context_data(**kwargs)
        instance['nombre_cabecera'] = 'Producto'
        instance['nombre_fomulario'] = 'Formulario para Crear Producto'
        return instance

