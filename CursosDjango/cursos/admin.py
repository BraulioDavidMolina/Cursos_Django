from django.contrib import admin
from .models import Cursos
# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('codigo', 'nombre', 'duracion', 'imagen')
    search_fields = ('nombre',)
    date_hierarchy = 'created'
    list_filter = ('duracion', 'nombre')

admin.site.register(Cursos, AdministrarModelo)