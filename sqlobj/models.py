# -*- coding:utf-8 -*-
from django.db import models
from sqlobj.conf import Question_type
# Create your models here.
from django.contrib.auth.models import User


class MyClass(models.Model):
    """班级表"""
    caption = models.CharField("班级", max_length=5)

    class Meta:
        db_table = 'class'


class MyStudent(models.Model):
    """学生表"""
    sname = models.CharField("姓名", max_length=3)
    gender = models.CharField("性别", max_length=1)
    myclass = models.ForeignKey(MyClass)

    class Meta:
        db_table = 'student'


class MyTeacher(models.Model):
    """老师表"""
    tname = models.CharField("姓名", max_length=3)

    class Meta:
        db_table = 'teacher'


class MyCourse(models.Model):
    """课程表"""
    cname = models.CharField("课程", max_length=3)
    myteacher = models.ForeignKey(MyTeacher)

    class Meta:
        db_table = 'course'


class MyScore(models.Model):
    """成绩表"""
    mystudent = models.ForeignKey(MyStudent)
    mycourse = models.ForeignKey(MyCourse)
    test = models.CharField("第几次考试", max_length=2)
    number = models.IntegerField("成绩", default=0)

    class Meta:
        db_table = 'score'


class Question(models.Model):
    """mysql题目"""
    QCLASS = ((1, 'sql语句'), (2, '选择题'))
    CHOICE = ((1, 'A'), (2, 'B'))
    text = models.CharField("题目", max_length=300)
    difficulty = models.IntegerField('难度等级', default=0)
    answernumber = models.IntegerField('答案个数', default=0)
    theanswer = models.CharField('答案', max_length=100)
    answersql = models.CharField('sql语句', max_length=300, default='')
    qclass = models.IntegerField('题目类型', choices=QCLASS, default=1)
    thechoice = models.IntegerField('选择', choices=CHOICE, default=1)
    achoice = models.CharField('A选项', max_length=20, default='')
    bchoice = models.CharField('B选项', max_length=20, default='')
    type = models.IntegerField("题目类型", choices=Question_type, default=0)
    info = models.CharField('备注', default='', max_length=20)


class Answer(models.Model):
    """答案"""
    question = models.ForeignKey(Question)
    sqltext = models.CharField('sql', max_length=500)
    usetime = models.FloatField('时间（毫秒）', default=0)
    name = models.CharField('大名', default='', max_length=4)
    good = models.IntegerField('赞', default=0)
    bad = models.IntegerField('踩', default=0)
