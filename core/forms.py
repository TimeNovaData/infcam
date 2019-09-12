from django import forms
from .models import Endereco


class EnderecoForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Endereco
        fields = [
            'cep',
            'logradouro',
            'complemento',
            'numero',
            'bairro',
            'pais',
            'estado',
            'cidade',
        ]