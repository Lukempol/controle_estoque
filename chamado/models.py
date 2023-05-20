from django.db import models
from django.utils import timezone

class Chamado(models.Model):
    tipo_chamado = [
        ( 1 , 'entrada'),
        ( 0 , 'saída' )
    ]
    cod = models.CharField(primary_key=True, max_length=30)
    tipo = models.CharField(max_length=20, choices=tipo_chamado)
    usuario = models.CharField(max_length=50)
    data = models.DateField(default=timezone.localdate(timezone.now()))
