from django.contrib import admin
from .models import Usuario
# Register your models here.
class UserioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido' ,'email', 'rol')
    ordering = ('rol',)

admin.site.register(Usuario, UserioAdmin)