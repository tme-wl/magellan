# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlobj', '0006_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='key_word',
            field=models.CharField(default='', max_length='30', null=True, verbose_name='关键字'),
        ),
        migrations.AddField(
            model_name='question',
            name='limit',
            field=models.IntegerField(default=0, null=True, verbose_name='题目限制'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.IntegerField(choices=[(1, '基础操作'), (2, '进阶练习')], default=0, verbose_name='题目等级类型'),
        ),
    ]
