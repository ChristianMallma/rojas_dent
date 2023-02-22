from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    keyword = models.CharField(verbose_name="Palabra clave", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['title']

    def __str__(self):
        return self.title
