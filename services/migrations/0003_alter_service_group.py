# Generated by Django 4.1.4 on 2023-03-15 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='group',
            field=models.CharField(default='', max_length=200, verbose_name='Grupo'),
        ),
    ]
