from decimal import Decimal
from django.db import models
from django.db.models import Sum, Max


# Create your models here.
class Museo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=50)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return (f"Nombre: {self.nombre}")

    def costo_total_produccion(self):
        total = self.guias.aggregate(total=Sum('exhibiciones__costo_produccion'))['total']

    costo_total_produccion.short_description = 'Costo total'

    def guias_mas_experiencia(self):
        """Retorna los nombres de los/las guía(s) con más años de experiencia
        en este museo, separados por coma si son varios.
        """
        agg = self.guias.aggregate(max_exp=Max('anios_experiencia_guia'))
        max_exp = agg.get('max_exp')
        if max_exp is None:
            return ''
        nombres = list(self.guias.filter(anios_experiencia_guia=max_exp)
                       .values_list('nombre_completo', flat=True))
        return ', '.join(nombres)

    guias_mas_experiencia.short_description = 'Guía(s) más experta(s)'


class Guia_de_museo(models.Model):
    nombre_completo = models.CharField(max_length=120)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=200)
    museo = models.ForeignKey(
        Museo, related_name='guias', on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Nombres: {self.nombre_completo} | Experiencia: {self.anios_experiencia_guia} años")


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=150)
    duracion_meses = models.PositiveIntegerField()
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    tematica = models.CharField(max_length=100)
    guia = models.ForeignKey(
        Guia_de_museo, related_name='exhibiciones', on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"Titulo: {self.titulo_exhibicion} | Meses: {self.duracion_meses} | "
            f"Costo: {self.costo_produccion} | Tematica: {self.tematica}")