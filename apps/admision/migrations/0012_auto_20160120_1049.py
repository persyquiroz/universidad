# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0011_encuesta_examen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_requisito', models.CharField(help_text='Ingrese la descripción del requisito', max_length=150, unique=True, verbose_name='Requisito')),
                ('detalles', models.TextField(blank=True, max_length=300, null=True, verbose_name='Detalles')),
            ],
        ),
        migrations.AlterField(
            model_name='encuesta_examen',
            name='coleg_acad_igles',
            field=models.CharField(blank=True, help_text='Referencial', max_length=200, null=True, verbose_name='Colegio/Academia/Iglesia'),
        ),
    ]
