from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class ClinicalCases(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    service = models.CharField(max_length=200, verbose_name='Servicio')
    image = models.ImageField(verbose_name='Imagen', upload_to='clinical_cases')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'caso clínico'
        verbose_name_plural = 'casos clínicos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ClinicalCasesDetail(models.Model):
    first_image = models.ImageField(verbose_name='Primera imagen', upload_to='clinical_cases')
    second_image = models.ImageField(verbose_name='Segunda imagen', upload_to='clinical_cases')
    third_image = models.ImageField(verbose_name='Tercera imagen', upload_to='clinical_cases')
    fourth_image = models.ImageField(verbose_name='Cuarta imagen', upload_to='clinical_cases')
    content = RichTextField(verbose_name="Contenido")
    clinical_case = models.ForeignKey(ClinicalCases, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'detalle de caso clínico'
        verbose_name_plural = 'detalles de casos clínicos'
        ordering = ['-created_at']

    def __str__(self):
        return ''
