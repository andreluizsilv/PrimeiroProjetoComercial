from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=150)
    ano = models.IntegerField()
    cor = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    data = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.placa