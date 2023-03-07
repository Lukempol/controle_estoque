from django.db import models
from django.db.utils import IntegrityError
from random import randint

class Produto(models.Model):
    cod = models.IntegerField(editable=False, primary_key=True)
    name = models.CharField(max_length=50)
    descricao = models.TextField()
    quantidade = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        try:
            self.cod = randint(1000,9999)
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(self, *args, **kwargs)
