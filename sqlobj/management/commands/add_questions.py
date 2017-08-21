# coding=utf-8

from django.core.management.base import BaseCommand

"""

"""

QUESTION_ANSWER = [
    ["学校一共有多少学生？", "select count(*) from student", "cont函数"],
    ["学校去掉重名的学生以后,有多少学生？", "select count(distinct sname) from student", "distinct用法"],
    ["一年级一班有多少学生？", "select count(*) from student where myclass_id =1", "where的用法"],
    ["一年级一班有多少女生？", "select count(*) from student where myclass_id = 1 and gender = '女' ", "where and用法"],
    ["一年级一班姓'王'的有多少同学？", "select count(*) from student where myclass_id = 1 and sname line'王%'", 'like和%的用法'],
    ["全校姓'王'或姓'李'的同学有多少人？", "select count(*) from student where sname like '王%' or sname like '李%'", 'or的用法'],
    ["一年级一班有多少姓'王'或姓'李'的同学？",
     "select count(*) from student where myclass_id = 1 and (sname like '王%' or sname like '李%')", 'and 和 or 的复用'],
    ["一年级一班有多少姓'王'的单姓(姓名为两个字)的同学？", "select count(*) from student where myclass_id == 1 and sname like '王_'",
     'like和_的用法'],
    ["一月份全校学生的平均成绩是多少？", "select avg(number) from source where test='一月'", 'avg的用法'],

]


class Command(BaseCommand):
    """把QUESTION_ANSWER里的问题和答案导入到数据库里，去掉重复的和已经导入的"""
    def handle(self, *args, **options):
        """"""
        pass