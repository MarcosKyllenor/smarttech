from django import forms
from .models import Produto

class formProduto (forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'preco', 'quantidade', 'fornecedor', 'imagem')
        
    def __init__(self, *args, **kwargs):
        super(formProduto, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})
        self.fields['preco'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['fornecedor'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagem'].widget.attrs.update({'class': 'form-control form-control-lg'})