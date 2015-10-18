# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Daten2', '0002_auto_20151013_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekttag',
            name='betreuer',
            field=models.ForeignKey(to='Daten2.Lehrer', null=True, related_name='betreuer', blank=True),
        ),
        migrations.AlterField(
            model_name='projekttag',
            name='raum',
            field=models.ForeignKey(to='Daten2.Raum', null=True, related_name='raum', blank=True),
        ),
    ]
