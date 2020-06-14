from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView)
from django.contrib.auth.decorators import login_required

from .precios import CalcularPrecios

from .models import Materiales, Producto, Categoria


from .forms import (MaterialesCreateForm,
                    CategoriaCreateForm,
                    ProductoCreateForm)


@login_required
def index(request):
    fn, ml, mp = CalcularPrecios()
    titulos = ['Producto','1-99','100-249','250-499','500-999','1000+']
    return render(request, 'precios.html', {'fn':fn, 
                                          'ml': ml,
                                          'mp': mp,
                                          'titulos':titulos})


# ========  MATERIALES ============

class MaterialesCreate(LoginRequiredMixin, CreateView):
    form_class = MaterialesCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('generales:index')

    def get_context_data(self, **kwargs):
        instance = super(MaterialesCreate, self).get_context_data(**kwargs)
        instance['nombre_cabecera'] = 'Materiales'
        instance['nombre_fomulario'] = 'Formulario para Crear Materiales'
        return instance


class MaterialesList(LoginRequiredMixin, ListView):
    model = Materiales
    template_name = 'generales/materiales_list.html'


class MaterialDetail(LoginRequiredMixin, DetailView):
    model = Materiales
    template_name = 'generales/materiales_detail.html'


class MaterialesUpdate(LoginRequiredMixin, UpdateView):
    model = Materiales
    form_class = MaterialesCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('generales:MaterialesList')


# =========== CATEGORIA =============

class CategoriaCreate(LoginRequiredMixin, CreateView):
    form_class = CategoriaCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('generales:index')

    def get_context_data(self, **kwargs):
        instance = super(CategoriaCreate, self).get_context_data(**kwargs)
        instance['nombre_cabecera'] = 'Categoria'
        instance['nombre_fomulario'] = 'Formulario para Crear Categorias'
        return instance

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'generales/categoria_list.html'
    
class CategoriaDetail(LoginRequiredMixin, DetailView):
    model = Categoria
    template_name = 'generales/categoria_detail.html'

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('generales:CategoriasList')



# ============= PRODUCTO =============

class ProductoCreate(LoginRequiredMixin,CreateView):
    form_class = ProductoCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        instance = super(ProductoCreate, self).get_context_data(**kwargs)
        instance['nombre_cabecera'] = 'Producto'
        instance['nombre_fomulario'] = 'Formulario para Crear Producto'
        return instance

class ProductoList(LoginRequiredMixin, ListView):
    model = Producto