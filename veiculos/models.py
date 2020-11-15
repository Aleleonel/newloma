from django.db import models
from django.urls import reverse_lazy

# from clientes.models import Cliente
from rastreadores.models import Rastreador


class Veiculos(models.Model):
    COR_CHOICES = (
        ("AZUL", "AZUL"),
        ("AMARELO", "Masculino"),
        ("BRANCO", "AMARELO"),
        ("PRETO", "PRETO"),
        ("PRATA", "PRATA"),
        ("BEGE", "BEGE"),
        ("VERMELHO", "VERMELHO"),
    )

    marca = models.CharField(max_length=60, null=False, blank=False)
    placa = models.CharField(max_length=7, unique=True, null=False, blank=False)
    chassi = models.CharField(max_length=17, unique=True, null=False, blank=False)
    ano_fab = models.CharField(max_length=4, null=False, blank=False)
    modelo = models.CharField(max_length=4, null=False, blank=False)
    renavam = models.CharField(max_length=11, null=False, blank=False)
    cor = models.CharField(max_length=25, choices=COR_CHOICES, null=False, blank=False)
    rastreador = models.OneToOneField(Rastreador, on_delete=models.SET_NULL, null=True)
    # clientes = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'veiculos'
        # ordering = ["-id"]

    def __str__(self):
        return self.placa

    def get_absolute_url(self):
        return reverse_lazy('veiculos:veiculos_detail', kwargs={'pk': self.pk})
