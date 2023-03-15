from django.db import models


# Create your models here.
class ClinicalCases(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    service = models.CharField(max_length=200, verbose_name='Servicio')
    image = models.ImageField(verbose_name='Imagen', upload_to='about')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'caso clínico'
        verbose_name_plural = 'casos clínicos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
