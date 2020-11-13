from django.db import models
from django.urls import reverse_lazy


class Prestador(models.Model):

    CATEGORIA_CHOICES = (
        ('MOTO', 'Moto'),
        ('MECANICA', 'Mecanica'),
        ('FUNILARIA', 'Funilaria'),
        ('VIDRO', 'Vidro'),
    )
    categoria = models.CharField(max_length=60, choices=CATEGORIA_CHOICES, null=True, blank=True)
    prestador = models.CharField(max_length=60, null=True, blank=True)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    bairro = models.CharField(max_length=60, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=True, blank=True)
    cep = models.CharField(max_length=60, null=True, blank=True)
    telefone2 = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = 'prestador'
        # ordering = ["-id"]

    def __str__(self):
        return self.prestador

    def get_absolute_url(self):
        return reverse_lazy('buscaprest:prestadores_detail', kwargs={'pk': self.pk})


