from django.urls import path

from .views import PrestaConfigCreate, SeleccionPresta

urlpatterns = [
            path('config/', PrestaConfigCreate.as_view(), name='PrestaConfigCreate'),
            path('select/', SeleccionPresta, name='SeleccionPresta'),
            ]       
