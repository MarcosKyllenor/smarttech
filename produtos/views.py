from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import formProduto
from .models import Produto

def produtos(request, sucesso=None, erro=None):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos, 'sucesso': sucesso, 'erro': erro})


def adicionar_produto(request):
    form = formProduto(request.POST, request.FILES)
    if request.method == 'GET':
        return render(request, 'adicionar_produto.html', {'form': form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            mensagem_sucesso = 'Produto adicionado com sucesso!'
            return redirect(reverse('produtos') + f'?sucesso={mensagem_sucesso}')
        else:
            print(form.errors)
            mensagem_erro = 'Falha ao adicionar produto!'
            return redirect(reverse('produtos') + f'?erro={mensagem_erro}')


def editar_produto(request, id):
    produto_id = get_object_or_404(Produto, id=id)
    if request.method == 'GET':
        form = formProduto(instance=produto_id)
        return render(request, "editar_produto.html", {'produto': produto_id, 'form': form})
    elif request.method == 'POST':
        save_form = formProduto(request.POST, request.FILES, instance=produto_id)
        if save_form.is_valid():
            save_form.save()
            mensagem_sucesso = 'Produto alterado com sucesso!'
            return redirect(reverse('produtos') + f'?sucesso={mensagem_sucesso}')
        else:
            print(save_form.errors)
            mensagem_erro = 'Falha ao editar produto!'
            return redirect(reverse('produtos') + f'?erro={mensagem_erro}')
        
    
def excluir_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    mensagem_sucesso = 'Produto excluido com sucesso!'
    return redirect(reverse('produtos') + f'?sucesso={mensagem_sucesso}')
