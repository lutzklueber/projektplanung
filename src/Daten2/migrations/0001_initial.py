# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fachrichtung',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Bezeichnung', models.CharField(max_length=20, verbose_name='Abteilung')),
            ],
            options={
                'verbose_name_plural': 'Fachrichtungen',
            },
        ),
        migrations.CreateModel(
            name='Klasse',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=20)),
                ('klassenstaerke', models.IntegerField(verbose_name='Staerke')),
                ('bemerkung', models.TextField(blank=True, verbose_name='Bemerkung')),
                ('fachrichtung', models.ForeignKey(to='Daten2.Fachrichtung')),
            ],
            options={
                'ordering': ['bezeichnung'],
                'verbose_name_plural': 'Klassen',
            },
        ),
        migrations.CreateModel(
            name='Klassentyp',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lehrer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nachname')),
                ('vorname', models.CharField(max_length=30, verbose_name='Vorname')),
                ('kurzel', models.CharField(max_length=5, verbose_name='Lehrerkuerzel')),
                ('stundenkontingent', models.IntegerField()),
                ('bemerkung', models.TextField(default=' ')),
                ('fachrichtung', models.ForeignKey(to='Daten2.Fachrichtung', verbose_name='Abteilung')),
            ],
            options={
                'ordering': ['kurzel', 'name'],
                'verbose_name_plural': 'Lehrer',
            },
        ),
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('projektthema', models.CharField(max_length=200)),
                ('bemerkung', models.TextField(blank=True)),
                ('agenda', models.TextField(blank=True)),
                ('mitglieder', models.IntegerField()),
                ('status', models.CharField(max_length=1, default='w', choices=[('w', 'Wunsch'), ('a', 'abgelehnt'), ('b', 'bewilligt'), ('u', 'unvollstaendig'), ('r', 'ruecksprache')])),
                ('besitzer', models.ForeignKey(blank=True, to='Daten2.Lehrer')),
                ('klasse', models.ForeignKey(default=1, to='Daten2.Klasse')),
            ],
            options={
                'ordering': ['klasse'],
                'verbose_name_plural': 'Projekte',
            },
        ),
        migrations.CreateModel(
            name='Projekttag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('betreuer', models.ForeignKey(related_name='betreuer', to='Daten2.Lehrer')),
            ],
            options={
                'verbose_name_plural': 'Projekttage',
            },
        ),
        migrations.CreateModel(
            name='Raum',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=20, verbose_name='Raum')),
                ('maxschueler', models.IntegerField(verbose_name='Anzahl Schueler')),
                ('bemerkung', models.TextField(blank=True, verbose_name='Bemerkung')),
                ('fachrichtung', models.ForeignKey(to='Daten2.Fachrichtung')),
            ],
            options={
                'ordering': ['bezeichnung'],
                'verbose_name_plural': 'Raeume',
            },
        ),
        migrations.CreateModel(
            name='Raumtyp',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['bezeichnung'],
                'verbose_name_plural': 'Raumtypen',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('wochentag', models.CharField(max_length=2)),
                ('wochentaglang', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Tage',
            },
        ),
        migrations.AddField(
            model_name='raum',
            name='raumtyp',
            field=models.ForeignKey(default=1, blank=True, to='Daten2.Raumtyp'),
        ),
        migrations.AddField(
            model_name='projekttag',
            name='raum',
            field=models.ForeignKey(related_name='raum', to='Daten2.Raum'),
        ),
        migrations.AddField(
            model_name='projekttag',
            name='tag',
            field=models.ForeignKey(to='Daten2.Tag'),
        ),
        migrations.AddField(
            model_name='projekt',
            name='projekttage',
            field=models.ManyToManyField(to='Daten2.Projekttag'),
        ),
        migrations.AddField(
            model_name='klasse',
            name='klassenlehrer',
            field=models.ForeignKey(to='Daten2.Lehrer'),
        ),
        migrations.AddField(
            model_name='klasse',
            name='klassentyp',
            field=models.ForeignKey(blank=True, to='Daten2.Klassentyp'),
        ),
    ]
