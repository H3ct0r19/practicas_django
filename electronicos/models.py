from django.db import models

class Electronico(models.Model):
    PREFIJOS = (
        ('M', 'Mega'),
        ('k', 'Kilo'),
        ('', ''),  # Sin prefijo
        ('m', 'Milli'),
        ('μ', 'Micro'),
        ('n', 'Nano'),
        ('p', 'Pico'),
    )
    UNIDADES = (
        ('Ω', 'Ohmios'),
        ('F', 'Faradios'),
        ('H', 'Henrios'),
        ('V', 'Voltios'),
        ('A', 'Amperios'),
        ('W', 'Vatios'),
    )
    
    nombre = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=1)
    prefijo = models.CharField(max_length=1, choices=PREFIJOS, blank=True)
    unidad = models.CharField(max_length=10, choices=UNIDADES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} de {self.valor}{self.prefijo}{self.unidad} (${self.precio})"
