from django.http import HttpResponse
from django.shortcuts import render
from chamado.models import Chamado
from chamado.mongoDB import mongo_conect
from chamado.form import get_produtos
from produto.models import Produto
from bson.objectid import ObjectId
import csv

def relatorio(request):
    template_name = "relatorio/relatorio_menu.html"
    return render(request, template_name)

def relatorio_produto(request):
    # Cria o objeto HttpResponse com o cabeçalho CSV apropriado.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename=relatorio_estoque.csv'},)

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

def relatorio_chamado(request):
    collection = mongo_conect()
    dict_nome = dict(get_produtos())
    # Cria o objeto HttpResponse com o cabeçalho CSV apropriado.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename=relatorio_chamado.csv'},)
    
    writer = csv.writer(response)
    writer.writerow(['Código', 'Título','Usuário', 'Data', 'Tipo de Chamado', 'Produto', 'Qauntidade'])
    
    for chamado in Chamado.objects.all().order_by('data'):
        product_list = collection.find_one({"_id" : ObjectId(chamado.cod)})
        product_list = product_list['lista']
        for item in product_list:
            writer.writerow([
                chamado.cod,
                chamado.titulo,
                chamado.usuario,
                chamado.data,
                chamado.tipoChamado,
                dict_nome[int(item['produto'])],
                item['qtd']
            ])
    return response

