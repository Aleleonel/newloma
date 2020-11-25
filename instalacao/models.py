from django.db import models
from django.urls import reverse_lazy

from instaladores.models import Instaladores


class Instalacao(models.Model):

    INSTALADO_CHOICES = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
        ('PENDENTE', 'PENDENTE')
    )

    ins_cliente = models.CharField('Associado', max_length=25, null=False, blank=False)
    inst_placa = models.CharField('Placa', max_length=7, unique=True, null=False, blank=False)
    ins_contrato = models.CharField('Contrato', max_length=25, null=True, blank=True)
    inst_data = models.DateTimeField('Data da Solicitação', False, True, editable=False)
    inst_instalador = models.ForeignKey(Instaladores, on_delete=models.SET_NULL, null=True)
    vendedor = models.CharField('Vendedor', max_length=25, null=False, blank=False)
    inst_data_fim = models.DateField('Data Instalação.', auto_now=False, null=True, blank=True)
    instalado = models.CharField(max_length=8, null=True, choices=INSTALADO_CHOICES, default=INSTALADO_CHOICES[1][1])
    inst_obs = models.TextField('Observação', max_length=300, null=True, blank=True)

    class Meta:
        db_table = 'instalacao'

    def __str__(self):
        return self.ins_cliente

    def get_absolute_url(self):
        return reverse_lazy('instalacao:instalacao_detail', kwargs={'pk': self.pk})