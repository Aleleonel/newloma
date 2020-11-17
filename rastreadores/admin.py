from django.contrib import admin
from .models import Rastreador


@admin.register(Rastreador)
class RatreadorAdmin(admin.ModelAdmin):
    list_display = [
        'nr_rastreador',
        'marca',
        'uso',
    ]
