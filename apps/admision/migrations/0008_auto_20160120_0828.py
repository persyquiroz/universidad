# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0007_auto_20160120_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_documento',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
