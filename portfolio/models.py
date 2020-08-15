from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    short_description = models.TextField(null=True, verbose_name="Descripción corta")
    long_description = models.TextField(null=True, verbose_name="Descripción larga")
    bg_image = models.ImageField(null=True, upload_to="projects", verbose_name="Imagen en fondo")
    list_image = models.ImageField(null=True, upload_to="projects", verbose_name="Imagen en lista")
    detail_image = models.ImageField(null=True, upload_to="projects", verbose_name="Imagen en detalle")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección web")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    short_description = models.TextField(verbose_name="Descripción corta")
    list_image = models.ImageField(null=True, upload_to="technologies", verbose_name="Imagen en lista")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Tecnología"
        verbose_name_plural = "Tecnologías"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
