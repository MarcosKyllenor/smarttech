from django import forms
from .models import Fornecedor

class FormFornecedor(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ('nome', 'documento', 'email', 'endereco', 'telefone')
        
    def __init__(self, *args, **kwargs):
        super(FormFornecedor, self).__init__(*args, **kwargs)  # Corrigido o nome da classe aqui
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['documento'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefone'].widget.attrs.update({'class': 'form-control'})
