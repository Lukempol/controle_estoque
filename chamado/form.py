from django import forms
from django.forms import formset_factory
from produto.models import Produto

def get_produtos():
    return [(pro.cod, pro.name) for pro in Produto.objects.all()]

dict_nome = dict(get_produtos())


class TipoForm(forms.Form):
    tipo_chamado = [
    ( 1 , 'Entrada de produtos'),
    ( 0 , 'Saída de produtos' )
    ]
    tipo = forms.ChoiceField(required=True, choices=tipo_chamado)

class TituloForm(forms.Form):
    titulo = forms.CharField(required=True, max_length=30)


class ProdutoForm(forms.Form):
    produtos = forms.ChoiceField(required=True, choices=get_produtos)
    qtd = forms.IntegerField(required=True, widget=forms.TextInput(attrs={"size": "5"}))

ProdutoFormSet = formset_factory(ProdutoForm, extra=1)