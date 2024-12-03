from django.db import models

# Create your models here.
class Consola(models.Model):
    TAMAÑOS = (
        ('Mb', 'Mb'),
        ('Gb', 'Gb'),
        ('Tb', 'Tb'),
    )
    
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    memoria = models.IntegerField()
    unidad_memoria = models.CharField(max_length=2, choices=TAMAÑOS)
    ram = models.IntegerField()
    unidad_ram = models.CharField(max_length=2, choices=TAMAÑOS)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} {self.modelo} con {self.memoria} {self.unidad_memoria} de almacenamiento y {self.ram} {self.unidad_ram} (${self.precio})"