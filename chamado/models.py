from django.db import models

class Chamado(models.Model):
    tipo_chamado = [
        ( 1 , 'entrada'),
        ( 0 , 'saída' )
    ]
    cod = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=20, choices=tipo_chamado)
    usuario = models.CharField(max_length=50)
    data = models.DateField()
