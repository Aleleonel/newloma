from django.db import models
from django.urls import reverse_lazy
from instaladores.models import Instaladores

import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('photos_vistorias', filename)


class Instalacao(models.Model):

    INSTALADO_CHOICES = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
        ('PENDENTE', 'PENDENTE')
    )
    VISTORIA_CHOICES = (
            ('SIM', 'SIM'),
            ('NÃO', 'NÃO'),
            ('PENDENTE', 'PENDENTE')
        )

    cliente = models.CharField('Associado', max_length=25, null=False, blank=False)
    placa = models.CharField('Placa', max_length=7, unique=True, null=False, blank=False)
    tel01 = models.CharField('Celular', max_length=11, null=True, blank=True)
    tel02 = models.CharField('Fone Res.', max_length=11, null=True, blank=True)
    data = models.DateTimeField('Data da Solicitação', False, True, editable=False)
    instalador = models.ForeignKey(Instaladores, on_delete=models.SET_NULL, null=True)
    vendedor = models.CharField('Vendedor', max_length=25, null=False, blank=False)
    data_fim = models.DateField('Data Instalação.', auto_now=False, null=True, blank=True)
    instalado = models.CharField(max_length=8, null=True, choices=INSTALADO_CHOICES, default=INSTALADO_CHOICES[1][1])
    vistoria = models.CharField(max_length=8, null=True, choices=VISTORIA_CHOICES, default=VISTORIA_CHOICES[1][1])
    obs = models.TextField('Observação', max_length=300, null=True, blank=True)
    imagens = models.FileField(upload_to=get_file_path)

    class Meta:
        db_table = 'instalacao'

    def __str__(self):
        return self.cliente

    def get_absolute_url(self):
        return reverse_lazy('instalacao:instalacao_detail', kwargs={'pk': self.pk})

    def get_abs_url(self):
        return reverse_lazy('instalacao:fotos_list', kwargs={'pk': self.pk})