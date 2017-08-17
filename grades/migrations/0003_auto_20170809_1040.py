# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_auto_20170809_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='cotation',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Cotação'),
        ),
        migrations.AlterField(
            model_name='question',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Nota'),
        ),
    ]