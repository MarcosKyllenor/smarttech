from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import FormFornecedor
from .models import Fornecedor
from produtos.models import Produto

def fornecedores(request, sucesso=None, erro=None):
    fornecedores = Fornecedor.objects.all()
    return render(request, "pages/fornecedores.html", {"fornecedores": fornecedores, "sucesso": sucesso, "erro": erro})


def adicionar_fornecedor(request):
    form = FormFornecedor(request.POST or None)
    if request.method == "GET":
        return render(request, "pages/adicionar_fornecedor.html", {"form": form})
    elif request.method == "POST":
        if form.is_valid():
            form.save()
            mensagem_sucesso = "Fornecedor adicionado com sucesso!"
            return redirect(reverse("fornecedores") + f"?sucesso={mensagem_sucesso}")
        else:
            print(form.errors)
            mensagem_erro = "Falha ao adicionar fornecedor!"
            return redirect(reverse("fornecedores") + f"?erro={mensagem_erro}")


def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == "GET":
        form = FormFornecedor(instance=fornecedor)
        return render(request, "pages/editar_fornecedor.html", {"fornecedor": fornecedor, "form": form})
    elif request.method == "POST":
        save_form = FormFornecedor(request.POST, instance=fornecedor)
        if save_form.is_valid():
            save_form.save()
            mensagem_sucesso = "Fornecedor alterado com sucesso!"
            return redirect(reverse("fornecedores") + f"?sucesso={mensagem_sucesso}")
        else:
            print(save_form.errors)
            mensagem_erro = "Falha ao editar fornecedor!"
            return redirect(reverse("fornecedores") + f"?erro={mensagem_erro}")


def excluir_fornecedor(request, id):
    # fornecedor = Fornecedor.objects.get(id=id)
    # fornecedor.delete()
    # mensagem_sucesso = "Fornecedor excluído com sucesso!"
    # return redirect(reverse("fornecedores") + f"?sucesso={mensagem_sucesso}")
    
    fornecedor = get_object_or_404(Fornecedor, id=id)
    produtos_vinculados = Produto.objects.filter(fornecedor=fornecedor)
    if produtos_vinculados.exists():
        mensagem_erro = "Não é possível excluir o fornecedor. Existem produtos vinculados a este fornecedor!"
        return redirect(reverse("fornecedores") + f"?erro={mensagem_erro}")
    else:
        fornecedor.delete()
        mensagem_sucesso = "Fornecedor excluído com sucesso!"
        return redirect(reverse("fornecedores") + f"?sucesso={mensagem_sucesso}")
