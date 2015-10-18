# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Daten2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekttag',
            name='betreuer',
            field=models.ForeignKey(to='Daten2.Lehrer', related_name='betreuer', blank=True),
        ),
        migrations.AlterField(
            model_name='projekttag',
            name='raum',
            field=models.ForeignKey(to='Daten2.Raum', related_name='raum', blank=True),
        ),
    ]
