from bson.objectid import ObjectId

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic

from chamado.models import Chamado
from chamado.form import ProdutoFormSet, TipoForm, TituloForm, dict_nome

from chamado.mongoDB import mongo_conect

from produto.models import Produto

class ChamadoListView(generic.ListView):
    model = Chamado
    queryset = Chamado.objects.all().order_by('data')

                  
def abreChamado(request):
    context = {'tipo' : TipoForm,
               'titulo' : TituloForm,
               }
    template_name = 'chamado/abertura.html'
    collection = mongo_conect()

    if request.method == 'GET':
        context['formset'] = ProdutoFormSet()

    if request.method == 'POST':
        context['formset'] = ProdutoFormSet(request.POST) 
        obj = request.POST
        chamado_list = []
        for i in range(int(obj['form-TOTAL_FORMS'])):
            i = str(i)
            prod = f'form-{i}-produtos'
            qtd = f'form-{i}-qtd'
            item_produto = { 'produto' : obj[prod],
                             'qtd' : obj[qtd] }
            chamado_list.append(item_produto)
        post = {
            'tipo' : obj['tipo'],
            'lista' : chamado_list
        }     
        post_id = collection.insert_one(post).inserted_id
        id = Chamado(cod = str(post_id), tipoChamado = obj['tipo'],titulo = obj['titulo'], usuario = request.user.username).save()

        if int(obj['tipo']) == 1:
            for itens in chamado_list:
                prodDB = Produto.objects.filter(cod=itens['produto']).first()
                prodDB.quantidade += int(itens['qtd'])
                prodDB.save()
        elif int(obj['tipo']) == 0:
            for itens in chamado_list:
                prodDB = Produto.objects.filter(cod=itens['produto']).first()
                prodDB.quantidade -= int(itens['qtd'])
                prodDB.save()
                
        print(obj, '\n', id)
        return redirect("chamado")                  
    return render(request, template_name, context)



def chamadoDetail(request, pk):
    template_name = 'chamado/chamado_detail.html'
    collection = mongo_conect()
    try:
        obj = Chamado.objects.get(pk=pk)
        product_list = collection.find_one({"_id" : ObjectId(pk)})
        product_list = product_list['lista']
    except:
        raise Http404
    
    product_name_list = []
    for item in product_list:
        cod = int(item['produto'])
        nome = dict_nome[cod]
        product_name_list.append({
            'produto' : nome,
            'qtd' : item['qtd']
        })

    context = {'object' : obj, 'product_list' : product_name_list}
    return render(request, template_name, context)



'''
def chamado(request):
    template_name='chamado.html'
    collection = mongo_conect()
    pointer = collection.find({'tipo' : 'mercearia'})
    #context = {'mongo' : pointer}
    return render(request, template_name, {'mongo' : pointer})
'''