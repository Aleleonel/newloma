from django.db import models
from django.urls import reverse_lazy

from endereco.models import Endereco


class Cliente(models.Model):
    VEICULO_CHOICES = (
        ("LEVE", "LEVE"),
        ("PESADO", "PESADO"),
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    nasc = models.DateField(null=True, blank=True)
    tel01 = models.CharField(max_length=11, null=False, blank=False)
    tel02 = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    contato = models.CharField(max_length=50, null=False, blank=False, unique=True)
    vtipo = models.CharField(max_length=6, choices=VEICULO_CHOICES, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    cadastro = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'cliente'
        # ordering = ["-id"]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('clientes:clientes_detail', kwargs={'pk': self.pk})
