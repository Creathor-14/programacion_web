from django.contrib import admin
from crud.models import Formulario,Principal,Postre,Bebestible

# Register your models here.
class datosFormulario(admin.ModelAdmin):
    list_display = ['nombre', 'paterno', 'materno', 'rut', 'email', 'comentarios']
    search_fields = ['nombre', 'rut', 'email']

class filtrarPrincipal(admin.ModelAdmin):
    list_filter=("categoria",)

class filtrarPostre(admin.ModelAdmin):
    list_filter=("categoria",)

class filtrarBebestible(admin.ModelAdmin):
    list_filter=("categoria",)

admin.site.register(Formulario,datosFormulario)
admin.site.register(Principal,filtrarPrincipal)
admin.site.register(Postre,filtrarPostre)
admin.site.register(Bebestible,filtrarBebestible)

