#cursos
from django.db import models

# Create your models here.
class Cursos(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.TextField(verbose_name="Nombre del cursos")
    duracion = models.IntegerField(verbose_name="Duracion del curso")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.nombre