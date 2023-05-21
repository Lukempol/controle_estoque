from django.db import models
from django.utils import timezone

class Chamado(models.Model):
    tipo_chamado = [
        ( 1 , 'Entrada de Produtos'),
        ( 0 , 'Saída de Produtos' )
    ]
    cod = models.CharField(primary_key=True, max_length=30)
    tipoChamado = models.IntegerField(choices=tipo_chamado)
    titulo = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    data = models.DateField(default=timezone.localdate(timezone.now()))
