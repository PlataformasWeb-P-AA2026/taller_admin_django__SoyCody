from decimal import Decimal
from django.db import models



# Create your models here.
class Museo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=50)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return (f"Nombre: {self.nombre}")

    def costo_total_produccion(self):
        total = Decimal('0.00')
        for guia in self.guias.all():
            for exhib in guia.exhibiciones.all():
                if exhib.costo_produccion is not None:
                    total += exhib.costo_produccion
        return total

    costo_total_produccion.short_description = 'Costo total producción'

    def guias_mas_experiencia(self):
        max_exp = None
        nombres = []
        for guia in self.guias.all():
            exp = guia.anios_experiencia_guia
            if max_exp is None or exp > max_exp:
                max_exp = exp
                nombres = [guia.nombre_completo]
            elif exp == max_exp:
                nombres.append(guia.nombre_completo)
        if not nombres:
            return ''
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