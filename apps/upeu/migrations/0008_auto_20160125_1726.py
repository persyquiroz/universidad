# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upeu', '0007_entidad_academica'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad_academica',
            name='direccion',
            field=models.CharField(blank=True, help_text='Dirección donde está ubicada', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entidad_academica',
            name='nombre_entidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='entidad_academica',
            name='tipo_universidad',
            field=models.ForeignKey(blank=True, help_text='Aplica solo a universidades', null=True, on_delete=django.db.models.deletion.CASCADE, to='upeu.Tipo_universidad'),
        ),
    ]
