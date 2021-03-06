# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeneaFamilyCore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='source',
            name='source_type',
            field=models.CharField(choices=[('G', 'Global'), ('N', 'Naissance'), ('D', 'Décès'), ('B', 'Baptême'), ('F', 'Famille'), ('U', 'Union'), ('M', 'Militaire')], max_length=1, verbose_name='Sourcer'),
        ),
    ]
