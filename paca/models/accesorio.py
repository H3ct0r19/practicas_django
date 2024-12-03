from django.db import models

# Create your models here.
class Accesorio(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f"Artículo {self.nombre} (${self.precio})"