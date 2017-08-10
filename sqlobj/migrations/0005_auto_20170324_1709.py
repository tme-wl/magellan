# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlobj', '0004_auto_20170322_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='achoice',
            field=models.CharField(default='', max_length=20, verbose_name='A选项'),
        ),
        migrations.AddField(
            model_name='question',
            name='bchoice',
            field=models.CharField(default='', max_length=20, verbose_name='B选项'),
        ),
    ]
