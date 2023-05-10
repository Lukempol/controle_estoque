from django.shortcuts import render
from django.views import generic

from chamado.models import Chamado
from chamado.form import ProdutoForm


class ChamadoListView(generic.ListView):
    model = Chamado
    queryset = Chamado.objects.all().order_by('data')


def abreChamado(request):
    context = {}
    context['form'] = ProdutoForm() 
    template_name = 'chamado/abertura.html'
    if request.GET:
        obj = request.GET['produtos']
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