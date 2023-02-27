from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=50)
    descrição = models.TextField()
    quantidade = models.IntegerField(default=0)


# Create your models here.
