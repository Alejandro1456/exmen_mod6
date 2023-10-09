from django.db import models

class Categoria(models.ModeL):
    nombre = models.CharField(max_length=100, unique=True)

class Productunits(models.TextChoices):
    UNIDAD = 'u', 'Unidades'
    KILOGRAMO = 'kg', 'kilogramos'
    LITRO = 'lt','litros'
    GRAMO = 'gr','gramos'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.Foreignkey(Categoria, on_delete=models. CASCADE)
    descripcion = models.TextField()
    precio = models.Decimalfield(decimal_places=2, max_digits=10)
    unidades = models.CharField(
        max_length=2,
        choices=Productunits.choices, 
        default=Productunits.UNIDAD
    )
    disponible = models.BooleanFiald(blank=True, default=True)
    created = models.DateTinefield(auto_nowadd=True)
    updated = models.DateTimeFleld(auto_o=True)