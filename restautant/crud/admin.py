from django.contrib import admin
from crud.models import Formulario,Principal

# Register your models here.
class datosFormulario(admin.ModelAdmin):
    list_display = ['nombre', 'paterno', 'materno', 'rut', 'email', 'comentarios']
    search_fields = ['nombre', 'rut', 'email']

class filtrarPrincipal(admin.ModelAdmin):
    list_filter=("categoria",)

admin.site.register(Formulario,datosFormulario)
admin.site.register(Principal,filtrarPrincipal)