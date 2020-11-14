from django.db import models
from django.urls import reverse_lazy


class Rastreador(models.Model):
    nr_rastreador = models.CharField(max_length=255)
    marca = models.CharField(max_length=25, null=True, blank=True)
    uso = models.BooleanField(default=False)

    class Meta:
        db_table = 'rastreador'
        # ordering = ["-id"]

    def __str__(self):
        return self.nr_rastreador

    def get_absolute_url(self):
        return reverse_lazy('rastreadores:rastreadores_detail', kwargs={'pk': self.pk})
