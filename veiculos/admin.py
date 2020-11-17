from django.contrib import admin
from .models import Veiculos


@admin.register(Veiculos)
class VeiculosAdmin(admin.ModelAdmin):
    list_display = [
        'marca',
        'placa',
        'chassi',
        'ano_fab',
        'modelo',
        'renavam',
    ]