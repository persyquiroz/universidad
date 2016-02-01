# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0013_auto_20160126_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan_acad_curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditos', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Número de créditos')),
                ('thp', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='THP')),
                ('hnp', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='HNP')),
                ('estado', models.CharField(max_length=1, verbose_name='Estado')),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Ciclo')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Curso')),
                ('plan_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Plan_academico')),
                ('pre_requisito', models.ForeignKey(blank=True, help_text='Curso pre-requisito', null=True, on_delete=django.db.models.deletion.CASCADE, to='academico.Plan_acad_curso')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='plan_acad_curso',
            unique_together=set([('plan_academico', 'ciclo', 'curso')]),
        ),
    ]
