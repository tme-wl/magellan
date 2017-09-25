# coding=utf-8

from django.core.management.base import BaseCommand
from sqlobj.models import Question
import logging
logger = logging.getLogger("magellan")

"""

"""
# [题目， 答案， info, 关键字]
QUESTION_ANSWER = [
    ["学校一共有多少学生？", """select count(*) from student""", "cont函数"],
    ["学校去掉重名的学生以后,有多少学生？", "select count(distinct sname) from student", "distinct用法"],
    ["一年级一班有多少学生？", "select count(*) from student,class where student.myclass_id =class.id and class.caption='一年级一班'",
     "where的用法"],

    ["一年级一班有多少女生？",
     "select count(*) from student,class where student.myclass_id =class.id and gender = '女' and class.caption='一年级一班'",
     "where and用法"],
    ["一年级一班姓'王'的有多少同学？",
     "select count(*) from student,class where student.myclass_id =class.id and class.caption='一年级一班' and sname like'王%'",
     'like和%的用法'],
    ["全校姓'王'或姓'李'的同学有多少人？", "select count(*) from student where sname like '王%' or sname like '李%'", 'or的用法'],
    ["一年级一班有多少姓'王'或姓'张'的同学？",
     "select count(*) from student,class where student.myclass_id =class.id and class.caption='一年级一班' and (sname like '王%' or sname like '张%')",
     'and 和 or 的复用'],

    ["全校有多少姓'王'的单姓(姓名为两个字)的同学？", "select count(*) from student where sname like '王_'",
     'like和_的用法'],
    ["半期全校学生的单科平均成绩是多少？", "select avg(number) from score where test='半期'", 'avg的用法'],
    ["全校语文期末平均成绩是多少？(不用join)",
     "select avg(a.number) from score a, course b where a.mycourse_id = b.id and b.cname='语文' and a.test = '期末'",
     '等价的用法', "-join"],
    ["全校语文期末平均成绩是多少？(用join)",
     "select avg(number) from score left join course on score.mycourse_id = course.id where course.cname='语文' and score.test='期末'",
     "join用法", "+join"],

    ["一年级一班期末语文成绩在80到100分(含边界)的有多少同学(between and)",
     "select count(*) from score,course,student,class where score.mycourse_id = course.id and score.mystudent_id=student.id and student.myclass_id=class.id and class.caption='一年级一班' and test ='期末' and cname='语文' and number between 80 and 100",
     "连表， between and",
     "+ between"
     ],

    ["半期考试中，语文成绩比数学高的同学有多少个？",
     "select count(*) from (select sname,number from student,score,course where score.mystudent_id=student.id and test='半期' and score.mycourse_id=course.id and cname = '语文') as a,(select sname,number from student,score,course where score.mystudent_id=student.id and test='半期' and score.mycourse_id=course.id and cname = '数学') as b where a.sname=b.sname and a.number > b.number",
     "连表,复合查询",
     ],

]


class Command(BaseCommand):
    """把QUESTION_ANSWER里的问题和答案导入到数据库里，去掉重复的和已经导入的"""

    def handle(self, *args, **options):
        """"""
        # 题目合集
        questions = [x.text for x in Question.objects.all()]
        qs_obj = []
        for add in QUESTION_ANSWER:
            if add[0] not in questions:
                print(add)
                if len(add) > 3:
                    qs_obj.append(Question(text=add[0], answersql=add[1], info=add[2], key_word=add[3]))
                else:
                    qs_obj.append(Question(text=add[0], answersql=add[1], info=add[2]))
        Question.objects.bulk_create(qs_obj)
        logger.info("新插入 {0} 条问题".format(len(qs_obj)))
