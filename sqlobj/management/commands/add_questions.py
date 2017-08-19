
from django.core.management.base import BaseCommand

"""

"""

QUESTION_ANSWER = {
    "": "",
}


class Command(BaseCommand):
    """把QUESTION_ANSWER里的问题和答案导入到数据库里，去掉重复的和已经导入的"""
    def handle(self, *args, **options):
        """"""
        pass