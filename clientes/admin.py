from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'cpf',
        'nasc',
        'tel01',
        'tel02',
        'email',
        'contato',
        'vtipo',
        'endereco',
        'cadastro'
    ]
