# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 07:49
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('start_date_is_approximately', models.BooleanField(default=False, help_text='Cochez, si la date est une approximation', verbose_name='Environ')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Date de fin')),
                ('end_date_is_approximately', models.BooleanField(default=False, help_text='Cochez, si la date est une approximation', verbose_name='Environ')),
                ('content', models.TextField(max_length=1000, null=True, verbose_name='Contenu')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ex: naissance, mariage, baptême, communion...', max_length=100, verbose_name="Type d'évenement")),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('time_period_type', models.CharField(choices=[('D', 'Date'), ('P', 'Durée')], help_text="\n\t\t<p><u>Aide:</u></p>\n\t\t<p> - Une Date est égale à une date de naissance\n\t\t(Ex: Né(e) le 01/01/2000).</p>\n\t\t<p> - Une durée est égale à un temps exercé dans un profession\n\t\t(Ex: Boulanger de 01/01/2000 à 31/01/2001).</p>\n\t\t<p>Attention: Après validation ce paramètre \n\t\tn'est plus modifiable !</p>", max_length=1, verbose_name='Type temporel')),
                ('description', models.CharField(blank=True, help_text="Description du type de l'èvenement", max_length=512)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='Pays')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Ville')),
                ('additional_address_information', models.CharField(blank=True, max_length=255, verbose_name="Complément d'information de l'adresse")),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ['country'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Prénom')),
                ('family_name', models.CharField(max_length=50, verbose_name='Nom de famille')),
                ('gender', models.CharField(choices=[('M', 'Homme'), ('W', 'Femme'), ('U', 'Inconnu(e)')], max_length=1, verbose_name='Genre')),
            ],
            options={
                'ordering': ['family_name'],
            },
        ),
        migrations.CreateModel(
            name='MemberEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneaFamilyCore.Event')),
                ('member_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneaFamilyCore.Member')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='family',
            name='father_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='father', to='GeneaFamilyCore.Member', verbose_name='Père'),
        ),
        migrations.AddField(
            model_name='family',
            name='mother_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mother', to='GeneaFamilyCore.Member', verbose_name='Mère'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneaFamilyCore.EventType', verbose_name="Type d'évènement"),
        ),
        migrations.AddField(
            model_name='child',
            name='child_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneaFamilyCore.Member'),
        ),
        migrations.AddField(
            model_name='child',
            name='family_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneaFamilyCore.Family'),
        ),
    ]