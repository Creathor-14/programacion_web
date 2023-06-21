from django.contrib import admin
from .models import Platform, VideoGame

# Register your models here.
class PlatformAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','platform')
    ordering = ('platform',)

class VideoGameAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idVideogame','title','studio','platform','value','stock')
    ordering = ('title',)

admin.site.register(Platform,PlatformAdmin)
admin.site.register(VideoGame,VideoGameAdmin)