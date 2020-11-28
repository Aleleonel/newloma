from django.db import models
from django.urls import reverse_lazy


class Instaladores(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    numero = models.CharField(max_length=5, null=True, blank=True)
    tel01 = models.CharField(max_length=11, null=True, blank=True)
    tel02 = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    preco = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        db_table = 'instaladores'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('instaladores:instaladores_detail', kwargs={'pk': self.pk})