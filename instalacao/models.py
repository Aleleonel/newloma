from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class Instalacao(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ins_cliente = models.CharField('Associado', max_length=25, null=False, blank=False)
    inst_placa = models.CharField('Placa', max_length=7, unique=True, null=False, blank=False)
    ins_contrato = models.CharField('Numero do contrato', max_length=25, null=True, blank=True)
    inst_data = models.DateField('Data Solicitação.', auto_created=True)
    inst_solicitante = models.CharField('Solicitação', max_length=25, null=True, blank=True)

    class Meta:
        db_table = 'instalacao'

    def __str__(self):
        return self.ins_cliente

    def get_absolute_url(self):
        return reverse_lazy('instalacao:instalacao_detail', kwargs={'pk': self.pk})