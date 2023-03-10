from django.db import models
from django.db.utils import IntegrityError
from random import randint
import unicodedata

class Produto(models.Model):
    tipos_produto =[
        (1, 'Padaria'),
        (2, 'Açougue'),
        (3, 'Mercearia'),
        (4, 'Congelados e frios'),
        (5, 'Hortifruti'),
        (6, 'Produtos de Limpeza'),
        (7, 'Higiene Pessoal'),
        (8, 'Bebidas'),
        (9, 'Papelaria')
    ]
    cod = models.IntegerField(editable=False, primary_key=True)
    name = models.CharField(max_length=50)
    simple_name = models.CharField(max_length=50, editable=False, default='')
    descricao = models.CharField(max_length=250, blank=True)
    quantidade = models.IntegerField(default=0)
    minimo = models.PositiveIntegerField(default=0)
    tipo = models.IntegerField(choices=tipos_produto, default=2)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.simple_name = unicodedata.normalize("NFD", self.name).encode("ascii", "ignore").decode("utf8").casefold()
        if self.cod:
            super().save(*args, **kwargs)
        else:
            try:
                self.cod = randint(1000,9999)
                super().save(*args, **kwargs)
            except IntegrityError:
                self.save(self, *args, **kwargs)
