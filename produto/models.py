from django.db import models
from django.db.utils import IntegrityError
from random import randint

class Produto(models.Model):
    cod = models.IntegerField(editable=False, primary_key=True)
    name = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    quantidade = models.IntegerField(default=0)
    minimo = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.cod:
            super().save(*args, **kwargs)
        else:
            try:
                self.cod = randint(1000,9999)
                super().save(*args, **kwargs)
            except IntegrityError:
                self.save(self, *args, **kwargs)
