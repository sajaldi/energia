# Generated by Django 5.1.7 on 2025-04-04 18:12

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_caracteristicamedicion_ambito_medicion_inferior_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangomedicion',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None, verbose_name='Color representativo'),
        ),
    ]
