# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upeu', '0008_auto_20160125_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad_academica',
            name='abreviatura',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='entidad_academica',
            name='tipo_universidad',
            field=models.ForeignKey(blank=True, help_text='Aplica solo a universidades', null=True, on_delete=django.db.models.deletion.CASCADE, to='upeu.Tipo_universidad'),
        ),
    ]