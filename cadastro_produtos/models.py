from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    fornecedor = models.ForeignKey('cadastro_fornecedores.Fornecedor',
                                   on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='', default='', null=True)

    def __str__(self):
        return self.nome
