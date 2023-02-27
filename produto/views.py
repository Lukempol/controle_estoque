from django.shortcuts import render
from django.views import generic
from produto.models import Produto

class ProdutoView(generic.ListView):
    model = Produto
    queryset = Produto.objects.all()
