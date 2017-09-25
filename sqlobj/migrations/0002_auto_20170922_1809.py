# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlobj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answersql',
            field=models.CharField(default='', verbose_name='sql语句', max_length=5000),
        ),
    ]
