from django.contrib import admin
from .models import Genero, Pelicula, Ticket
from .utils import formato_clp
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
 list_display = ("nombre",)
 search_fields = ("nombre",)
@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
 list_display = ("titulo", "genero", "clasificacion", "duracion_min", "precio_clp",
 "en_cartelera")
 list_filter = ("genero",)
 search_fields = ("titulo",)
 @admin.display(description="Precio", ordering="precio")
 def precio_clp(self, obj):
    return formato_clp(obj.precio)
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
 list_display = ("codigo", "pelicula", "nombre_comprador", "cantidad", "total_clp",
 "fecha_compra")
 list_filter = ("pelicula",)
 search_fields = ("codigo", "nombre_comprador", "correo")
 readonly_fields = ("codigo", "fecha_compra")
 @admin.display(description="Total")
 def total_clp(self, obj):
    return formato_clp(obj.total)
