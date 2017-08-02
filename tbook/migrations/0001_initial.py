# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50, verbose_name='Designação')),
                ('school', models.CharField(max_length=200, verbose_name='Escola')),
                ('year_in_school', models.CharField(choices=[('7ºano', '7º Ano'), ('8ºano', '8º Ano'), ('9ºano', '9º Ano'), ('10ºano', '10º Ano'), ('11ºano', '11º Ano'), ('12ºano', '12º Ano')], default='7º Ano', max_length=100, verbose_name='Ano')),
                ('max_students', models.IntegerField(default=25, verbose_name='máx alunos')),
            ],
            options={
                'verbose_name_plural': 'Turmas',
                'ordering': ['designation'],
                'verbose_name': 'Turma',
            },
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200, verbose_name='Designação')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('birth_date', models.DateField(verbose_name='data de Nascimento')),
                ('tutor', models.CharField(max_length=100, verbose_name='Enc.Educação')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbook.SchoolClass')),
            ],
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='school_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbook.SchoolYear'),
        ),
    ]
