# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Daten2', '0006_auto_20151018_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lehrer',
            name='bemerkung',
            field=models.TextField(default=' ', blank=True),
        ),
    ]
