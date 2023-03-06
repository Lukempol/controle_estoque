from django.shortcuts import render
from django.views import generic
from produto.models import Produto
from .forms import ProdutoForm

class ProdutoListView(generic.ListView):
    model = Produto
    queryset = Produto.objects.all()

def ProdutoDetail(request, pk):
    template_name = 'produto/produto_detail.html'
    #obj = Produto.objects.get(pk=pk)
    context = {'object': pk}
    return render(request, template_name, context)
    

class CreateProduto(generic.edit.CreateView):
    form_class = ProdutoForm
    success_url = '/'
    template_name = 'produto/create_produto.html'
    model = Produto
