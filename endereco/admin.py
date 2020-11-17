from django.contrib import admin
from .models import Endereco


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
        'rua',
        'numero',
        'complemento',
        'bairro',
        'cidade',
        'pais'
    ]