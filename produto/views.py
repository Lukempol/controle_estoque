from django.shortcuts import render
from django.views import generic
from produto.models import Produto
from .forms import ProdutoForm

import csv
from django.http import HttpResponse

def relatorio(request):
    # Cria o objeto HttpResponse com o cabeçalho CSV apropriado.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename=relatorio.csv'},)

    writer = csv.writer(response)
    writer.writerow(['Código', 'Nome', 'Status', 'Estoque', 'Estoque Mínimo', 'Descrição'])
    for obj in Produto.objects.all():
        status = 'Estoque OK' if obj.quantidade > obj.minimo else 'Estoque Baixo' if obj.quantidade > 0 else 'Em Falta'
        writer.writerow([
            obj.cod, 
            obj.name, 
            status, 
            obj.quantidade,
            obj.minimo,
            obj.descricao
            ])

    return response

class ProdutoListView(generic.ListView):
    model = Produto
    queryset = Produto.objects.all().order_by('simple_name')

def ProdutoDetail(request, pk):
    template_name = 'produto/produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)
    

class CreateProduto(generic.CreateView):
    form_class = ProdutoForm
    success_url = '/produto/'
    template_name = 'produto/create_produto.html'
    model = Produto


class EditProduto(generic.UpdateView):
    model = Produto
    template_name = 'produto/create_produto.html'
    form_class = ProdutoForm
    success_url = '/produto/'

class DeleteProduto(generic.DeleteView):
    model = Produto
    #template_name = 'produto/create_produto.html'
    success_url = '/produto/'
