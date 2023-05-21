from django.urls import path
from django.contrib.auth.decorators import login_required
from relatorio import views


urlpatterns = [
    path('', views.relatorio, name='relatorio'),
    path('produto/', login_required(views.relatorio_produto), name='relatorio_produto'),
    path('chamado/', login_required(views.relatorio_chamado), name='relatorio_chamado'),

]