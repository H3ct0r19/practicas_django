from django.db import models

# Create your models here.
class Servicio(models.Model):
    PLANES = (
        ('Mensual', 'Mensual'),
        ('Trimestral', 'Trimestral'),
        ('Semestral', 'Semestral'),
        ('Anual', 'Anual'),
    )
    nombre = models.CharField(max_length=50)
    plan = models.CharField(max_length=20, choices=PLANES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} {self.plan} (${self.precio})"