from django.shortcuts import render
from django.views import generic

from chamado.models import Chamado
from chamado.form import ProdutoFormSet, TipoForm

from chamado.mongoDB import mongo_conect

class ChamadoListView(generic.ListView):
    model = Chamado
    queryset = Chamado.objects.all().order_by('data')

                  
def abreChamado(request):
    context = {'tipo' : TipoForm}
    template_name = 'chamado/abertura.html'
    #if request.GET:
    if request.method == 'GET':
        context['formset'] = ProdutoFormSet()
    if request.method == 'POST':
        context['formset'] = ProdutoFormSet(request.POST) 
        #obj = request.GET['produtos']
        obj = request.POST#['form-0-produtos']
        '''
        chamado_list = []
        for i in range(int(obj['form-TOTAL_FORMS'])):
            i = str(i)
            prod = f'form-{i}-produtos'
            qtd = f'form-{i}-qtd'
            item_produto = { obj[prod] : obj[qtd] }
            chamado_list.append(item_produto)
        post = {
            'tipo' : obj['tipo'],
            'lista' : chamado_list
        } 
        collection = mongo_conect()
        post_id = str(collection.insert_one(post).inserted_id)
        id = Chamado(cod = post_id, tipo = obj['tipo'], usuario = request.user.username).save()
        print(id)             
'''
        print(obj)
    return render(request, template_name, context)


'''
def chamado(request):
    template_name='chamado.html'
    collection = mongo_conect()
    pointer = collection.find({'tipo' : 'mercearia'})
    #context = {'mongo' : pointer}
    return render(request, template_name, {'mongo' : pointer})
'''