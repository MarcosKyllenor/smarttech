from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome