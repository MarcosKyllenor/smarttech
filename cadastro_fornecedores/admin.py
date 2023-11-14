from django.contrib import admin
from .models import Fornecedor


class cadastro_fornecedores_admin(admin.ModelAdmin):
    ...


admin.site.register(Fornecedor, cadastro_fornecedores_admin)