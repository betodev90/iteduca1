# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-22 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_auto_20180422_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=10),
        ),
    ]
