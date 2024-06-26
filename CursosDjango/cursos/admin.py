from django.contrib import admin
from .models import Cursos
from .models import Actividad
# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('codigo', 'nombre', 'duracion', 'imagen')
    search_fields = ('nombre',)
    date_hierarchy = 'created'
    list_filter = ('duracion', 'nombre')

admin.site.register(Cursos, AdministrarModelo)


class AdministrarActividad(admin.ModelAdmin):
    readonly_fields = ('created','clave')
    list_display = ('clave', 'nombre', 'curso', 'descripcion')
    search_fields = ('nombre', 'curso')
    date_hierarchy = 'created'
    list_filter = ('curso', 'created')

admin.site.register(Actividad, AdministrarActividad)