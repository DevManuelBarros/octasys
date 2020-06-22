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


from .models import PrestaConfig
from .forms import PrestaConfigCreateForm

from django.conf import settings

from .interPresta import get_dataApi

#===============PrestaCofig==========
class PrestaConfigCreate(LoginRequiredMixin, CreateView):
    form_class = PrestaConfigCreateForm
    template_name = 'generales/create_form_small.html'
    success_url = reverse_lazy('generales:index')
    def get_context_data(self, **kwargs):
        instance = super(PrestaConfigCreate, self).get_context_data(**kwargs)
        instance['nombre_cabecera'] = 'PrestaConfig'
        instance['nombre_fomulario'] = 'Formulario para Configuraciones de Presta'
        return instance

@login_required
def SeleccionPresta(request):
    sesiones = PrestaConfig.objects.all()
    if request.method == 'POST':
        settings.SESION_PRESTA = int(request.POST.get('sesion', False))
    sesion_actual = PrestaConfig.objects.filter(pk=settings.SESION_PRESTA)[0]       
    return render(request, 'presta/seleccion.html', {'context' : sesiones, 'sp' : sesion_actual})

@login_required
def VerPresta(request):
    context = get_dataApi
    return render(request, 'presta/ver.html', {'context' : context}) 