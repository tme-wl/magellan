# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlobj', '0003_question_answersql'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qclass',
            field=models.IntegerField(choices=[(1, 'sql语句'), (2, '选择题')], verbose_name='题目类型', default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='thechoice',
            field=models.IntegerField(choices=[(1, 'A'), (2, 'B')], verbose_name='选择', default=1),
        ),
    ]
