# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0002_modalidad_estudio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidad_examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad_examen', models.CharField(max_length=100)),
            ],
        ),
    ]
