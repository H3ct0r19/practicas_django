from django.contrib import admin
from .models.prenda import Prenda
from .models.accesorio import Accesorio

# Register your models here.
admin.site.register(Prenda)
admin.site.register(Accesorio)
