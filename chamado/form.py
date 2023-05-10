from django import forms
from django.forms import formset_factory
from produto.models import Produto

def get_produtos():
    return [(pro.cod, pro.name) for pro in Produto.objects.all()]

'''
class ProdutoForm(forms.Form):
    produtos = forms.ModelChoiceField(choices= get_produtos)
'''

class ProdutoForm(forms.Form):
    produtos = forms.ChoiceField(choices=get_produtos)

ProdutoFormSet = formset_factory(ProdutoForm, extra=1)