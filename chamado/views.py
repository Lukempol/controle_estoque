from django.shortcuts import render
from django.views import generic

from chamado.models import Chamado
from chamado.form import ProdutoFormSet


class ChamadoListView(generic.ListView):
    model = Chamado
    queryset = Chamado.objects.all().order_by('data')


def abreChamado(request):
    context = {}
    template_name = 'chamado/abertura.html'
    #if request.GET:
    if request.method == 'GET':
        context['formset'] = ProdutoFormSet()
    if request.method == 'POST':
        context['formset'] = ProdutoFormSet(request.POST) 
        #obj = request.GET['produtos']
        obj = request.POST#['form-0-produtos']
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