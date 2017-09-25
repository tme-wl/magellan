# -*- coding:utf-8 -*-
import random
from sqlobj.models import MyClass, MyStudent, MyTeacher, MyCourse, MyScore
from django.core.management.base import BaseCommand
import logging
import time
import sys

logger = logging.getLogger("magellan")

first_name = [
    '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '李', '张', '刘',
    '冯', '陈', '蒋', '沈', '韩', '杨', '王', '李', '张', '刘',
    '朱', '许', '何', '吕', '张', '王', '李', '张', '刘',
    '孔', '曹', '金', '魏', '陶', '姜', '王', '张', '刘', '陈',
    '谢', '邹', '柏', '窦', '章', '王', '张', '刘',
    '苏', '潘', '范', '彭', '李',
    '鲁', '马', '李',
    '唐', '马', '刘', '陈',
    '罗', '马'
]
middle_name = [
    "惟", "我", "家", "谱", "履", "历", "备", "详", "原", "籍", "海", "州", "肇", "始", "武", "昌",
    "明", "初", "来", "照", "相", "宅", "河", "北", "天", "启", "开", "科", "崇", "祯", "任", "职", "乡", "贤", "名", "宦",
    "德", "言", "事", "功", "显", "扬", "令", "绪", "繁", "育", "兴", "隆", "聿", "愿", "同", "心", "孝", "敬",
    "和", "睦", "世", "代", "绵", "长", '龙',
    "丕", "承", "祖", "泽",
]

last_name = [
    '博', '竹', '阳', '军', '萱', '飞', '荨', '含', '若', '雨', '鸣', '春', '文', '默', '杰',
    '海', '旭', '烁', '琪', '涵', '晴', '萍', '婷', '平', '龙', '胡', '谟', '辰', '来', '株',
    '花', '莲', '敏', '妍', '静', '馨', '韵', '欣', '媛', '泽', '蕾', '淯', '沧', '娟', '诚',
    '朋', '凡', '楠', '宁', '杨', '然', '浩', '菡', '一', '宸', '政', '菲', '闻', '夫', '轩',
    '宇', '翠', '熙', '月', '明', '凯', '瑶', '雅', '炜', '茜', '雯', '怡', '江', '强', '鑫',
    '林', '瑜', '麟', '惜', '希', '曦', '晏', '懿', '琴', '芝', '芙', '君', '兹', '晨', '恒',
    '畅', '郡', '彰', '诰', '荣', '津', '旗', '飒', '语', '瑔', '晃', '悦', '赫', '铭', '永',
    '伦', '友', '昆', '沅', '昊', '皓', '桐', '冉', '予', '于', '哲', '丽', '洛', '尉', '升',
    '丞', '羽', '方', '汐', '勇', '果', '易', '森', '辉', '鹏', '耀', '腾', '霖', '昙', '珍',
    '炎', '彦', '逸', '盛', '柏', '旺', '扬', '曜', '硕', '瑄', '栋', '朔', '翔', '捷', '桀',
    '帅', '茧', '谱', '巍', '菁', '航', '亮', '仪', '焱', '齐', '嘉', '琳', '玥', '焓', '烨',
    '恺', '颐', '楚', '旌', '茹', '锐', '姿', '霭', '峥', '睿', '福', '琼', '斌', '珏', '舒',
    '翼', '安', '佑', '绎', '潍', '毅', '浚', '翌', '洋', '潮', '桃', '香', '小', '唐', '黔',
    '譞', '鸿', '尧', '释', '亨', '仁', '孝', '言', '函', '坤', '天', '芳', '奕', '冠', '育',
    '昶', '泉', '晶', '映', '年', '立', '远', '贤', '妃', '淇', '梦', '沛', '彤', '运', '迎',
    '敖', '松', '云', '吉', '骁', '寇', '乐', '颖', '冲', '昂', '澍', '彭', '汇', '红', '伟',
    '全', '昌', '冬', '达', '澜', '蕊', '璇', '销', '演', '逊', '勋', '歌', '晓', '宏', '源',
    '沦', '汛', '智', '躍', '洲', '培', '才', '华', '漪', '雪', '昱', '淼', '清', '帆', '丹',
    '珊', '紫', '嫣', '姗', '笑', '童', '瑞', '浦', '和', '德', '瀚', '睦', '滨', '滔', '玺',
    '琦', '豪', '涛', '润', '秦', '美', '彬', '雄', '顺', '民', '康', '邦', '婕', '英', '赐',
    '祺', '越', '钰', '初', '咚', '圳', '太', '审', '溢', '铨', '慧', '靖', '田', '原', '诺',
    '晖', '好', '成', '虎', '胜', '翰', '岚', '露', '觅', '庭', '致', '志', '峰', '光', '新',
    '娜', '尹', '城', '萌', '沣']

my_class = []
num = ["一", "二", "三", "四", "五", "六"]
cl = ["一", "二", "三"]
for i in num:
    for j in cl:
        my_class.append("%s年级%s班" % (i, j))

# 必修课，每个学生必选
course_required = ["语文", "数学", "外语"]
# 选修课，每个学生任选三门
# course_elective = ['体育', "美术", "手工课", "音乐", "实验课"]

exam_name = ["半期", '期末']


def choice_name():
    """生成一个名字"""
    a = first_name[random.randint(0, len(first_name)) - 1]
    b = middle_name[random.randint(0, len(middle_name)) - 1]
    c = last_name[random.randint(0, len(last_name)) - 1]
    m = random.randint(0, 1)
    if m:
        return a + c
    else:
        return a + b + c


def create_class():
    """创建class表"""
    logger.info("create class data")
    MyClass.objects.bulk_create([MyClass(caption=my_class[i]) for i in range(len(my_class))])
    logger.info("create class end")


def create_student():
    """插入学生数据"""
    logger.info("create student data")
    student_obj = []
    my_class = MyClass.objects.all()
    id = 1
    for cla in my_class:
        for st in range(random.randint(20, 25)):
            # 一个班30 - 40人
            student_obj.append(MyStudent(sname=choice_name(), gender=random.choice(["男", "女"]), myclass_id=cla.id))
    MyStudent.objects.bulk_create(student_obj)
    logger.info("create student end")


def create_teacher():
    """
    创建教师表
    course_required 必修课 全校每门必修课安排6个老师
    """
    logger.info("create teacher data")
    id = 1
    teacher = []
    for co in course_required:
        coid = MyCourse.objects.get(cname=co).id
        for i in range(6):
            teacher.append(MyTeacher(tname=choice_name(), mycourse_id=coid))
            id += 1
    MyTeacher.objects.bulk_create(teacher)
    logger.info("create teacher end")


def create_course():
    """
    创建课程表

    """
    logger.info("create course data")
    course = []
    id = 1
    for co in course_required:
        course.append(MyCourse(cname=co))
        id += 1
    MyCourse.objects.bulk_create(course)
    logger.info("create course end")


def create_score():
    """
    创建成绩表
    :return: 
    """
    logger.info("create score data")
    students = MyStudent.objects.all()
    courses = MyCourse.objects.all()
    score = []
    id = 1
    for st in students:
        # 学生
        for co in courses:
            # 课程
            for exam in exam_name:
                # 考试
                score.append(MyScore(mystudent_id=st.id, mycourse_id=co.id, test=exam, number=random.randint(50, 100)))
    MyScore.objects.bulk_create(score)
    logger.info("create score end")


class Command(BaseCommand):
    """把QUESTION_ANSWER里的问题和答案导入到数据库里，去掉重复的和已经导入的"""
    def handle(self, *args, **options):
        """"""
        print("delete data")
        MyClass.objects.all().delete()
        MyCourse.objects.all().delete()
        MyTeacher.objects.all().delete()
        MyStudent.objects.all().delete()
        MyScore.objects.all().delete()
        print("run create_teacher")
        a = time.time()
        create_class()
        create_student()
        create_course()
        create_teacher()
        create_score()
        print(time.time() - a)
        print("end create_teacher")
