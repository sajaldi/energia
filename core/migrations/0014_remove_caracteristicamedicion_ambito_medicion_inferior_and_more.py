# Generated by Django 5.1.7 on 2025-04-04 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_puntomedicion_ambito_medicion_inferior_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracteristicamedicion',
            name='ambito_medicion_inferior',
        ),
        migrations.RemoveField(
            model_name='caracteristicamedicion',
            name='ambito_medicion_superior',
        ),
        migrations.RemoveField(
            model_name='caracteristicamedicion',
            name='valor_objetivo',
        ),
        migrations.CreateModel(
            name='RangoMedicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_min', models.FloatField(verbose_name='Valor mínimo')),
                ('valor_max', models.FloatField(verbose_name='Valor máximo')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('color', models.CharField(blank=True, max_length=20, null=True, verbose_name='Color representativo')),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rangos', to='core.caracteristicamedicion')),
            ],
            options={
                'verbose_name': 'Rango de Medición',
                'verbose_name_plural': 'Rangos de Medición',
                'ordering': ['caracteristica', 'valor_min'],
            },
        ),
        migrations.AddField(
            model_name='documentomedicion',
            name='rango',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.rangomedicion', verbose_name='Rango aplicable'),
        ),
    ]
