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


class MyCourse(models.Model):
    """课程表"""
    cname = models.CharField("课程", max_length=3)

    class Meta:
        db_table = 'course'


class MyTeacher(models.Model):
    """老师表"""
    tname = models.CharField("姓名", max_length=3)
    # 老师教的课程
    mycourse = models.ForeignKey(MyCourse)

    class Meta:
        db_table = 'teacher'


class MyScore(models.Model):
    """成绩表"""
    mystudent = models.ForeignKey(MyStudent)
    mycourse = models.ForeignKey(MyCourse)
    test = models.CharField("第几次考试", max_length=2)
    number = models.IntegerField("成绩", default=0)

    class Meta:
        db_table = 'score'


class Question(models.Model):
    """
    mysql题目
    
    题目分两种, 一种为选择题，a b 两个选项，
    一种为答题，自行输入sql语句
    答题状态下，应该有必须用什么关键字，以及不能用什么关键字等限制
    """
    QCLASS = ((1, 'sql语句'), (2, '选择题'))
    CHOICE = ((1, 'A'), (2, 'B'))
    text = models.CharField("题目", max_length=300)
    # 难度级别，可让用户选择
    number = models.IntegerField("排序ID", default=1)
    difficulty = models.IntegerField('难度等级', default=0)
    answernumber = models.IntegerField('答案个数', default=0)
    theanswer = models.CharField('答案', max_length=100)
    answersql = models.CharField('sql语句', max_length=5000, default='')
    qclass = models.IntegerField('题目类型', choices=QCLASS, default=1)
    thechoice = models.IntegerField('选择', choices=CHOICE, default=1)
    achoice = models.CharField('A选项', max_length=20, default='')
    bchoice = models.CharField('B选项', max_length=20, default='')
    # 题目等级类型,进阶 入门 成长，提升等
    type = models.IntegerField("题目等级类型", choices=Question_type, default=0)
    # 限制 0不限制 1为必须键入关键字 2为不能使用关键字
    limit = models.IntegerField("题目限制", default=0, null=True)
    key_word = models.CharField("关键字", max_length='30', default='', null=True)
    # 题目备注
    info = models.CharField('备注', default='', max_length=20)


class Answer(models.Model):
    """答案"""
    question = models.ForeignKey(Question)
    sqltext = models.CharField('sql', max_length=500)
    usetime = models.FloatField('时间（毫秒）', default=0)
    name = models.CharField('大名', default='', max_length=4)
    good = models.IntegerField('赞', default=0)
    bad = models.IntegerField('踩', default=0)
