from django.http import HttpResponse
from django.shortcuts import render


def cadastroProduto(request):
    return render(request, 'cadastroProduto.html')


def listarProdutos(request):
    return render(request, 'produtos.html')
