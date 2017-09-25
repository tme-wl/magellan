# coding=utf-8

from django.core.management.base import BaseCommand
from sqlobj.models import Question


class Command(BaseCommand):
    """把QUESTION_ANSWER里的问题和答案导入到数据库里，去掉重复的和已经导入的"""

    def handle(self, *args, **options):
        """"""
        # 题目合集
        questions = Question.objects.all().order_by("id")
        id = 1
        for i in questions:
            i.number = id
            id += 1
            i.save()

