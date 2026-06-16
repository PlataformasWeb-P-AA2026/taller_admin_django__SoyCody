from django.contrib import admin
from .models import Museo, Guia_de_museo, Exhibicion

# Register your models here.
admin.site.register(Museo)
admin.site.register(Guia_de_museo)
admin.site.register(Exhibicion)