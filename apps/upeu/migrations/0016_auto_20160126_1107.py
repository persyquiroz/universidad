# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upeu', '0015_auto_20160126_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad_academica',
            name='tipo_universidad',
            field=models.ForeignKey(blank=True, help_text='Aplica solo a universidades', null=True, on_delete=django.db.models.deletion.CASCADE, to='upeu.Tipo_universidad'),
        ),
    ]
