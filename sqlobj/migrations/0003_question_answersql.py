# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlobj', '0002_auto_20170302_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answersql',
            field=models.CharField(verbose_name='sql语句', default='', max_length=300),
        ),
    ]
