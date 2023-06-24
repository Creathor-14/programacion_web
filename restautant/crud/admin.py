from django.contrib import admin

from crud.models import Formulario,Plato

# Register your models here.

class datosFormulario(admin.ModelAdmin):
    list_display=("rut","nombre","ap_paterno","ap_materno","comentario")
    search_fields=("rut","ap_paterno")

class filtrarPlatos(admin.ModelAdmin):
    list_filter=("categoria",)
admin.site.register(Formulario,datosFormulario)
admin.site.register(Plato,filtrarPlatos)