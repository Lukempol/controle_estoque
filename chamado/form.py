from django import forms
from django.forms import formset_factory
from produto.models import Produto

def get_produtos():
    return [(pro.cod, pro.name) for pro in Produto.objects.all()]



class TipoForm(forms.Form):
    tipo_chamado = [
    ( 1 , 'entrada'),
    ( 0 , 'saída' )
    ]
    tipo = forms.ChoiceField(required=True, choices=tipo_chamado)

class ProdutoForm(forms.Form):
    produtos = forms.ChoiceField(required=True, choices=get_produtos)
    qtd = forms.IntegerField(required=True)

ProdutoFormSet = formset_factory(ProdutoForm, extra=1, can_delete=True)