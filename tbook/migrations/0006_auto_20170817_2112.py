# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 21:12
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tbook', '0005_auto_20170815_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(default='media/fotos_alunos/no-img.jpg', upload_to='media/fotos_alunos/', verbose_name='Foto'),
        ),
    ]