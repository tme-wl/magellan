# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sqltext', models.CharField(verbose_name='sql', max_length=500)),
                ('usetime', models.IntegerField(verbose_name='时间（毫秒）', default=0)),
                ('name', models.CharField(default='', verbose_name='大名', max_length=4)),
                ('good', models.IntegerField(verbose_name='赞', default=0)),
                ('bad', models.IntegerField(verbose_name='踩', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MyClass',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('caption', models.CharField(verbose_name='班级', max_length=5)),
            ],
            options={
                'db_table': 'class',
            },
        ),
        migrations.CreateModel(
            name='MyCourse',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('cname', models.CharField(verbose_name='课程', max_length=3)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='MyScore',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('test', models.CharField(verbose_name='第几次考试', max_length=2)),
                ('number', models.IntegerField(verbose_name='成绩', default=0)),
                ('mycourse', models.ForeignKey(to='sqlobj.MyCourse')),
            ],
            options={
                'db_table': 'score',
            },
        ),
        migrations.CreateModel(
            name='MyStudent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sname', models.CharField(verbose_name='姓名', max_length=3)),
                ('gender', models.CharField(verbose_name='性别', max_length=1)),
                ('myclass', models.ForeignKey(to='sqlobj.MyClass')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='MyTeacher',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('tname', models.CharField(verbose_name='姓名', max_length=3)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(verbose_name='题目', max_length=300)),
                ('difficulty', models.IntegerField(verbose_name='难度等级', default=0)),
                ('answernumber', models.IntegerField(verbose_name='答案个数', default=0)),
                ('theanswer', models.CharField(verbose_name='答案', max_length=100)),
                ('info', models.CharField(default='', verbose_name='备注', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='myscore',
            name='mystudent',
            field=models.ForeignKey(to='sqlobj.MyStudent'),
        ),
        migrations.AddField(
            model_name='mycourse',
            name='myteacher',
            field=models.ForeignKey(to='sqlobj.MyTeacher'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='sqlobj.Question'),
        ),
    ]
