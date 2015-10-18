# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Daten2', '0005_auto_20151015_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekt',
            name='besitzer',
            field=models.ForeignKey(to='Daten2.Lehrer'),
        ),
    ]
