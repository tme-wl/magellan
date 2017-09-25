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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('sqltext', models.CharField(verbose_name='sql', max_length=500)),
                ('usetime', models.FloatField(verbose_name='时间（毫秒）', default=0)),
                ('name', models.CharField(verbose_name='大名', max_length=4, default='')),
                ('good', models.IntegerField(verbose_name='赞', default=0)),
                ('bad', models.IntegerField(verbose_name='踩', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('caption', models.CharField(verbose_name='班级', max_length=5)),
            ],
            options={
                'db_table': 'class',
            },
        ),
        migrations.CreateModel(
            name='MyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cname', models.CharField(verbose_name='课程', max_length=3)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='MyScore',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tname', models.CharField(verbose_name='姓名', max_length=3)),
                ('mycourse', models.ForeignKey(to='sqlobj.MyCourse')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.CharField(verbose_name='题目', max_length=300)),
                ('difficulty', models.IntegerField(verbose_name='难度等级', default=0)),
                ('answernumber', models.IntegerField(verbose_name='答案个数', default=0)),
                ('theanswer', models.CharField(verbose_name='答案', max_length=100)),
                ('answersql', models.CharField(verbose_name='sql语句', max_length=300, default='')),
                ('qclass', models.IntegerField(verbose_name='题目类型', choices=[(1, 'sql语句'), (2, '选择题')], default=1)),
                ('thechoice', models.IntegerField(verbose_name='选择', choices=[(1, 'A'), (2, 'B')], default=1)),
                ('achoice', models.CharField(verbose_name='A选项', max_length=20, default='')),
                ('bchoice', models.CharField(verbose_name='B选项', max_length=20, default='')),
                ('type', models.IntegerField(verbose_name='题目等级类型', choices=[(1, '基础操作'), (2, '进阶练习')], default=0)),
                ('limit', models.IntegerField(verbose_name='题目限制', null=True, default=0)),
                ('key_word', models.CharField(verbose_name='关键字', max_length='30', null=True, default='')),
                ('info', models.CharField(verbose_name='备注', max_length=20, default='')),
            ],
        ),
        migrations.AddField(
            model_name='myscore',
            name='mystudent',
            field=models.ForeignKey(to='sqlobj.MyStudent'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='sqlobj.Question'),
        ),
    ]
