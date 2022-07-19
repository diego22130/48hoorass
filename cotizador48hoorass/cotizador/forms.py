from cProfile import label
from unicodedata import name
from django import forms
from .models import Cotizador


class CotizadorForm(forms.ModelForm):

    class Meta:
        model = Cotizador
        fields = ['categoryplans', 'origin', 'destination',
                  'dates', 'numPax', 'typeDocument', 'numdocument', 'age']
        widgets = {
            'categoryplans': forms.Select(attrs={'class': 'pais'}),
            'origin': forms.Select(attrs={'class': 'pais'}),
            'destination': forms.Select(attrs={'class': 'pais'}),
            'dates': forms.TextInput(attrs={'class': 'input-text', 'name': 'dates', 'placeholder': 'Selecciona tu fecha', 'autocomplete': 'off'}),
            'numPax': forms.Select(attrs={'class': 'pais'}),
            'typeDocument': forms.Select(attrs={'class': 'pais'}),
            'numdocument': forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Digite su documento', 'autocomplete': 'off'}),
            'age': forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Digite su edad', 'autocomplete': 'off'}),
        }
