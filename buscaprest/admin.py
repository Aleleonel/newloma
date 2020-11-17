from django.contrib import admin
from .models import Prestador


@admin.register(Prestador)
class Prestador(admin.ModelAdmin):
    list_display = [
        'categoria',
        'prestador',
        'endereco',
        'bairro',
        'cidade',
        'cep'

    ]
