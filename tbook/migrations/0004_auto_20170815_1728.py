# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbook', '0003_auto_20170814_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='foto',
            field=models.ImageField(default='static/fotos_alunos/no-img.jpg', upload_to='static/fotos_alunos/', verbose_name='Foto'),
        ),
    ]
