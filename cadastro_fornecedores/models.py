from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome