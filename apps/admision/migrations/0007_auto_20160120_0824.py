# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0006_auto_20160120_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_documento',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
    ]
