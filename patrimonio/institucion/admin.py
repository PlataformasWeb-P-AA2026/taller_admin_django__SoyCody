from django.contrib import admin
from .models import Museo, Guia_de_museo, Exhibicion


@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'ciudad',
        'anio_fundacion',
        'costo_total_produccion',
        'guias_mas_experiencia',
    )


admin.site.register(Guia_de_museo)
admin.site.register(Exhibicion)