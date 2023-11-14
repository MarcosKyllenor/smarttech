from django.http import HttpResponse
from django.shortcuts import render


def cadastroFornecedor(request):
    return render(request, 'pages/cadastroFornecedor.html')


def listarFornecedores(request):
    return render(request, 'pages/listarFornecedores.html')