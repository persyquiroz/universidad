# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upeu', '0011_auto_20160126_0936'),
        ('academico', '0003_periodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan_academico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_plan', models.CharField(blank=True, max_length=60, null=True, unique=True, verbose_name='Número de plan')),
                ('estado', models.CharField(max_length=1, verbose_name='Estado')),
                ('entidad_academica', models.ForeignKey(help_text='Escuela profesional o entidad académica', on_delete=django.db.models.deletion.CASCADE, to='upeu.Entidad_academica')),
            ],
        ),
        migrations.AlterField(
            model_name='periodo',
            name='abierto',
            field=models.CharField(help_text='Use 1 parar abierto, 0 para cerrado', max_length=1, verbose_name='Abierto'),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='fecha_inicio',
            field=models.DateField(verbose_name='Fecha de inicio'),
        ),
        migrations.AddField(
            model_name='plan_academico',
            name='periodo',
            field=models.ForeignKey(help_text='Periodo académico', on_delete=django.db.models.deletion.CASCADE, to='academico.Periodo'),
        ),
    ]
