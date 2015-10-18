# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Daten2', '0003_auto_20151013_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projektbetreuer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('betreuer', models.ForeignKey(related_name='betreuer', to='Daten2.Lehrer')),
                ('tag', models.ForeignKey(to='Daten2.Tag')),
            ],
            options={
                'verbose_name_plural': 'Projektbetreuer',
            },
        ),
        migrations.CreateModel(
            name='Projektraum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('raum', models.ForeignKey(related_name='raum', to='Daten2.Raum')),
                ('tag', models.ForeignKey(to='Daten2.Tag')),
            ],
            options={
                'verbose_name_plural': 'Projektraeume',
            },
        ),
        migrations.RemoveField(
            model_name='projekttag',
            name='betreuer',
        ),
        migrations.RemoveField(
            model_name='projekttag',
            name='raum',
        ),
        migrations.RemoveField(
            model_name='projekttag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='projekt',
            name='projekttage',
        ),
        migrations.DeleteModel(
            name='Projekttag',
        ),
        migrations.AddField(
            model_name='projekt',
            name='projektbetreuer',
            field=models.ManyToManyField(to='Daten2.Projektbetreuer'),
        ),
        migrations.AddField(
            model_name='projekt',
            name='projektraeume',
            field=models.ManyToManyField(to='Daten2.Projektraum'),
        ),
    ]
