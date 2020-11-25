from django.db import models
from django.urls import reverse_lazy

from endereco.models import Endereco


class Instaladores(models.Model):
    nome = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25, unique=True)
    rg = models.CharField(max_length=25, unique=True)
    tel01 = models.CharField(max_length=25)
    tel02 = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField()
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    preco = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'instaladores'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('instaladores:instaladores_detail', kwargs={'pk': self.pk})
