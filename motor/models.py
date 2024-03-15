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


class InformacionFinanciera(models.Model):
    ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    egresos = models.DecimalField(max_digits=10, decimal_places=2)
    activos = models.DecimalField(max_digits=10, decimal_places=2)
    pasivos = models.DecimalField(max_digits=10, decimal_places=2)
    historial_crediticio = models.TextField(null = True, blank = True)
    puntuacion_crediticia = models.IntegerField(null = True, blank = True)
    antiguedad_laboral = models.IntegerField()
    tipo_empleo = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    numero_dependientes = models.IntegerField(default=0)
    historial_bancario = models.TextField(null=True, blank=True)
    garantias = models.TextField(null=True, blank=True)
    tipo_vivienda = models.CharField(max_length=100)
    educacion = models.CharField(max_length=100)
    

    def __str__(self):
        return self.ingresos
    class Meta:
        verbose_name = 'InformacionFinanciera'
        verbose_name_plural = 'InformacionFinanciera'
        ordering = ['ingresos']