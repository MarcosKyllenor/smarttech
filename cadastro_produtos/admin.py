from django.contrib import admin
from .models import Produto


class cadastro_produto_admin(admin.ModelAdmin):
    ...


admin.site.register(Produto, cadastro_produto_admin)