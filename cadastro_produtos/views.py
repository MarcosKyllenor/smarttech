from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import formCadastroProduto

def cadastroProduto(request, sucesso=None, erro=None):
    form = formCadastroProduto()
    return render(request, 'cadastroProduto.html', {'form': form, 'sucesso': sucesso, 'erro': erro})

def form_cadastro_produto(request):
    form = formCadastroProduto(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        mensagem_sucesso = 'Produto cadastrado com sucesso!'
        return redirect(reverse('cadastroProduto') + f'?sucesso={mensagem_sucesso}')
    else:
        print(form.errors)
        mensagem_erro = 'Falha ao cadastrar produto!'
        return redirect(reverse('cadastroProduto') + f'?erro={mensagem_erro}')

def listarProdutos(request):
    return render(request, 'produtos.html')
