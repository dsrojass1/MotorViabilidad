from django.db import models

class Oferta(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tasa = models.DecimalField(max_digits=5, decimal_places=2)
    franquicia = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.tipo) + ' ' + self.monto
    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'
        ordering = ['monto']