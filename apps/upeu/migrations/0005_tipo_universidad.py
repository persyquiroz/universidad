# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upeu', '0004_distrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_universidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, unique=True)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]