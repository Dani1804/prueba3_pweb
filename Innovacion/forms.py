# myapp/forms.py
from django import forms
from .models import Contacto

class contactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'asunto','mensaje']
