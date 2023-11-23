from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from cadastro_fornecedores.views import (
    fornecedores,
    adicionar_fornecedor,
    editar_fornecedor,
    excluir_fornecedor,
)
from produtos.views import produtos, adicionar_produto, editar_produto, excluir_produto
from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("addfornecedor/", adicionar_fornecedor, name="adicionar_fornecedor"),
    path("fornecedores/", fornecedores, name="fornecedores"),
    path("fornecedores/adicionar/", adicionar_fornecedor, name="adicionar_fornecedor"),
    path("fornecedores/editar/<int:id>/", editar_fornecedor, name="editar_fornecedor"),
    path(
        "fornecedores/excluir/<int:id>/", excluir_fornecedor, name="excluir_fornecedor"
    ),
    path("produtos/", produtos, name="produtos"),
    path("produtos/adicionar/", adicionar_produto, name="adicionar_produto"),
    path("produtos/editar/<int:id>/", editar_produto, name="editar_produto"),
    path("produtos/excluir/<int:id>/", excluir_produto, name="excluir_produto"),
    path("", home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
