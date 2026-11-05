import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
class Genero(models.Model):
 nombre = models.CharField(max_length=60, unique=True)
 class Meta:
    verbose_name = "género"
    verbose_name_plural = "géneros"
    ordering = ["nombre"]
    def __str__(self):
        return self.nombre
class Pelicula(models.Model):
    titulo = models.CharField("título", max_length=150)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name="peliculas",
    verbose_name="género")
    sinopsis = models.TextField()
    duracion_min = models.PositiveIntegerField("duración (minutos)")
    clasificacion = models.CharField("clasificación", max_length=20)
    fecha_estreno = models.DateField("fecha de estreno")
    afiche = models.ImageField(upload_to="afiches/")
    precio = models.PositiveIntegerField("precio de la entrada (CLP)")
    en_cartelera = models.BooleanField("en cartelera", default=True)
    class Meta:
        verbose_name = "película"
        verbose_name_plural = "películas"
        ordering = ["titulo"]
    def __str__(self):
        return self.titulo
def generar_codigo():
    return uuid.uuid4().hex[:8].upper()
class Ticket(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name="tickets",
    verbose_name="película")
    nombre_comprador = models.CharField("nombre del comprador", max_length=100)
    correo = models.EmailField("correo electrónico")
    cantidad = models.PositiveSmallIntegerField(
    "cantidad de entradas",
    validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    fecha_compra = models.DateTimeField("fecha y hora de compra", auto_now_add=True)
    codigo = models.CharField("código", max_length=8, unique=True, default=generar_codigo,
    editable=False)
    class Meta:
        ordering = ["-fecha_compra"]
    @property
    def total(self):
        return self.cantidad * self.pelicula.precio
    def __str__(self):
        return f"Ticket {self.codigo} - {self.pelicula.titulo}"