from django.db import models


# Create your models here.
class About(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Nombres')
    profession = models.TextField(verbose_name='Profesión')
    image = models.ImageField(verbose_name='Imagen', upload_to='about')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'nosotros'
        verbose_name_plural = 'nosotros'
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name
