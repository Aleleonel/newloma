from django.db import models
from django.urls import reverse_lazy


class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'endereco'
        # ordering = ["-id"]

    def __str__(self):
        return self.rua

    def get_absolute_url(self):
        return reverse_lazy('endereco:enderecos_detail', kwargs={'pk': self.pk})
