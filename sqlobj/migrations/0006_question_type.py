# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlobj', '0005_auto_20170324_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.IntegerField(default=0, choices=[(1, '基础操作'), (2, '进阶练习')], verbose_name='题目类型'),
        ),
    ]
