from django import forms
from .models import PrestaConfig

class_control = {'class' : 'form-control'}
class_control_required = {'class' : 'form-control', 'required' : True}
#============ MATERIALES =================
class PrestaConfigCreateForm(forms.ModelForm):
    class Meta:
        model = PrestaConfig
        fields = ('__all__')
        widget = {
            'name'      : forms.TextInput(attrs=class_control_required),
            'host'      : forms.TextInput(attrs=class_control_required),
            'protocol'  : forms.Select(attrs=class_control),
            'key'       : forms.TextInput(attrs=class_control_required),
            'active'    : forms.BooleanField(),
            'default'   : forms.BooleanField(),
        }