from django.shortcuts import render

def home(request):
    template_name='home.html'
    return render(request, template_name)

def chamado(request):
    template_name='chamado.html'
    return render(request, template_name)