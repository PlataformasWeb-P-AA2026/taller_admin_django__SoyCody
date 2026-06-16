from django.db import models

# Create your models here.
class Museo(models.Model):
    nombre=models.CharField(max_length=30, null=False)
    ciudad=models.CharField()
    año_fundacion=models.IntegerField()

    def __str__(self):
        return (f"Nombre: {self.nombre} | Ciudad: {self.ciudad} | Año de fundación: {self.año_fundacion}")
    
class Guia_de_museo(models.Model):
    opcionIdioma=(
        ('Español', 'Español'),
        ('Ingles', 'Ingles'),
        ('Portugues', 'Portugues'),
        ('Ruso', 'Ruso')
        )
    nombre_competo=models.CharField()
    años_experiencia_guia=models.IntegerField()
    idiomas_hablados=models.Charfield(choices=opcionIdioma)
    # la idea de opcionIdiomas fue sacado de repositorio CLASE002-BIM/ejemplo04 
    museo=models.ForeignKey(Museo, related_name='museo', on_delete=models.CASCADE)

    def __str__(self):
        return (f"Nombres Completos: {self.nombre_competo} | Experiencia: {self.años_experiencia_guia} años")
