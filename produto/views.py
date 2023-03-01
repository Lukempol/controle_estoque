from django.shortcuts import render
from django.views import generic
from produto.models import Produto
from .forms import ProdutoForm

class ProdutoView(generic.ListView):
    model = Produto
    queryset = Produto.objects.all()

class CreateProduto(generic.edit.CreateView):
    form_class = ProdutoForm
    success_url = '/'
    template_name = 'produto/create_produto.html'
    model = Produto
