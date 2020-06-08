from django import forms
from .models import (Materiales,
                     Categoria,
                     Producto)



class_control = {'class' : 'form-control'}
class_control_required = {'class' : 'form-control', 'required' : True}
#============ MATERIALES =================
class MaterialesCreateForm(forms.ModelForm):
    class Meta:
        model = Materiales
        fields = ('__all__')
        widget = {
                    'nombre'            : forms.TextInput(attrs=class_control_required),
                    'descripcion'       : forms.Textarea(attrs=class_control),
                    'costo'             : forms.NumberInput(attrs=class_control),
                    'unidad_de_medida'  : forms.Select(attrs=class_control),
                 }



#============ CATEGORIA ===================
class CategoriaCreateForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('__all__')
        widget = {
                    'nombre' : forms.TextInput(attrs=class_control_required),
                    'descripcion' : forms.Textarea(attrs=class_control),
                    'peso' : forms.BooleanField(),
                    'medida1' : forms.BooleanField(),
                    'medida2' : forms.BooleanField(),
                    'medida1_int' : forms.BooleanField(),
                    'medida2_int' : forms.BooleanField(),
                    'medida1_ext' : forms.BooleanField(),
                    'medida2_ext' : forms.BooleanField(),
                    'caras' : forms.BooleanField(),
                 }

#==============PRODUCTO ================

class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('__all__')
        
        widget = {
            'nombre' : forms.TextInput(attrs=class_control_required),
            'peso' : forms.NumberInput(attrs=class_control_required),
            'material' : forms.Select(attrs=class_control),
            'categoria' : forms.Select(attrs=class_control),
            'forma' : forms.Select(attrs=class_control),
            'medida1' : forms.NumberInput(attrs=class_control_required),
            'medida2' : forms.NumberInput(attrs=class_control),
            'medida1_int' : forms.NumberInput(attrs=class_control),
            'medida2_int' : forms.NumberInput(attrs=class_control),
            'medida1_ext' : forms.NumberInput(attrs=class_control),
            'medida2_ext' : forms.NumberInput(attrs=class_control),
            'descripcion' : forms.Textarea(attrs=class_control),
            'caras' :forms.Select(attrs=class_control),
        }