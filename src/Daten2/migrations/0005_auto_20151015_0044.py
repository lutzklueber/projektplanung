# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Daten2', '0004_auto_20151013_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekt',
            name='mitglieder',
            field=models.IntegerField(default=20),
        ),
    ]
