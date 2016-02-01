# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0012_remove_plan_acad_curso_ht'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plan_acad_curso',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='plan_acad_curso',
            name='ciclo',
        ),
        migrations.RemoveField(
            model_name='plan_acad_curso',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='plan_acad_curso',
            name='plan_academico',
        ),
        migrations.RemoveField(
            model_name='plan_acad_curso',
            name='pre_requisito',
        ),
        migrations.DeleteModel(
            name='Plan_acad_curso',
        ),
    ]
