# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0005_tipo_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_documento',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
