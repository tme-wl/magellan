# -*- coding:utf-8 -*-
import random
from django.db import connections
import sys
print (sys.getdefaultencoding())

"""
六个年级，每个年级六个班，每个班500-600人，每个学生十三门课,(十门必修三门选修)，每门课共五次考试。
每个老师教一门学科的三个班。
"""

first_name = [
 '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '李', '张','刘',
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
for i in num:
    for j in num:
        my_class.append("%s年%s班" % (i, j))

#必修课，每个学生必选
course_required = ["语文", "数学", "外语", "历史", "地理", "生物", "物理", "化学", "政治", '体育']
#选修课，每个学生任选三门
course_elective = ['计算机', "美术", "手工课", "音乐", "实验课"]

exam_name = ["一月", "二月", "三月", "四月", "五月",'六月','七月','八月','九月','十月','期末']


import csv
class_path = '/Users/tme/Desktop/myclass.csv'
student_path  = '/Users/tme/Desktop/mystudent.csv'
teacher_path = '/Users/tme/Desktop/myteacher.csv'
source_path = '/Users/tme/Desktop/mysource.csv'
score_path = '/Users/tme/Desktop/myscore.csv'


def choice_name():
    """生成一个名字"""
    a = first_name[random.randint(0, len(first_name))-1]
    b = middle_name[random.randint(0, len(middle_name))-1]
    c = last_name[random.randint(0, len(last_name))-1]
    m = random.randint(0, 1)
    if m:
        return a+c
    else:
        return a+b+c


def create_class_csv():
    print('create class data')
    with open(class_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(("id", "caption"))
        temp = []
        id_number = 1
        for the_class in my_class:
            temp.append((str(id_number), the_class))
            id_number += 1
        writer.writerows(temp)
    print('end create data')



def create_class(cur):
    """插入年级数据"""
    print("create class data")
    class_name = []
    temp = []
    for the_class in my_class:
        temp .append("('" + the_class + "'),")
        class_name.append(the_class)
    temp[-1]=temp[-1][:-1]
    sql = "insert into class (caption) values %s " % (" ".join(temp))
    print(sql)
    cur.execute(sql)
    print("end create data")


def create_student_csv(cur):
    sex =['男', '女']
    sql ="select id,caption from class"
    cur.execute(sql)
    print("create student data")
    classdata = cur.fetchall()
    with open(student_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(("id", "sname", "gender", "myclass_id"))
        id_number = 1
        for one in classdata:
            temp = []
            for i in range(random.randint(300,400)):
                temp.append((id_number,choice_name(),random.choice(sex),one[0]))
                id_number += 1
            writer.writerows(temp)
    print("end create data")

def create_student(cur):
    """插入学生数据"""
    sex =['男', '女']
    sql ="select id,caption from class"
    cur.execute(sql)
    print("create student data")
    classdata = cur.fetchall()
    for one in classdata:
        for i in range(random.randint(300,400)):
            sql = "insert into student (sname,gender,myclass_id) values ('%s','%s',%d)" % (choice_name(), random.choice(sex), one[0])
            print(sql)
            cur.execute(sql)
    print("end create data")


def create_teacher_csv():
    print("create teacher data")
    temp = []
    id_number = 1
    while len(temp) < (len(course_required) + len(course_elective)) * 6 * 2:
        temp.append((id_number, choice_name()))
        id_number += 1
    with open(teacher_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(("id", "tname"))
        writer.writerows(temp)
    print('end create data')



def create_teacher(cur):
    """插入老师数据"""
    print("create teacher data")
    temp = []
    teacher_name = []
    while len(temp) < (len(course_required) + len(course_elective)) * 6 * 2:
        #一个学科老师教三个班，一个年级要13*2个老师，六个年级
        teacher = choice_name()
        if teacher not in temp:
            temp.append("('" + teacher + "'),")
            teacher_name.append(teacher)
    temp[-1]=temp[-1][:-1]
    sql = "insert into teacher (tname) values %s " % (" ".join(temp))
    print(sql)
    cur.execute(sql)
    print("end create data")


def create_cource_csv(cur):
    sql = "select id, tname from teacher"
    cur.execute(sql)
    allteacher = cur.fetchall()
    print("create course data")
    number = 0
    course_number = 0
    id_number = 1
    course = course_required + course_elective
    temp = []
    for t in allteacher:
        temp.append((id_number, course[course_number], t[0]))
        id_number += 1
        #sql = "insert into course(cname,myteacher_id) values ('%s', %d)" % (course[course_number], t[0])
        #print(sql)
        #cur.execute(sql)
        number += 1
        if number == 12:
            number = 0
            course_number += 1
    with open(source_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(("id", "cname", 'myteacher_id'))
        writer.writerows(temp)
    print("end create data")


def create_course(cur):
    """插入课程表"""
    sql = "select id, tname from teacher"
    cur.execute(sql)
    allteacher = cur.fetchall()
    print("create course data")
    number = 0
    course_number = 0
    course = course_required + course_elective
    for t in allteacher:
        sql = "insert into course(cname,myteacher_id) values ('%s', %d)" % (course[course_number], t[0])
        print(sql)
        cur.execute(sql)
        number += 1
        if number == 12:
            number = 0
            course_number += 1
    print("end create data")


def create_score_csv(cur):
    coursesql = "select id, cname, myteacher_id from course order by cname"
    cur.execute(coursesql)
    courseobj = cur.fetchall()
    coursedict = {}
    for co in courseobj:
        if co[1] not in coursedict:
            coursedict[co[1]] = [co[0],co[0],co[0]]
        else:
            coursedict[co[1]].append(co[0])
            coursedict[co[1]].append(co[0])
            coursedict[co[1]].append(co[0])
    '''
    coursedict={
        '语文'：[老师1，老师1，老师1，老师2，老师2，老师2]
        ...
    }
    '''
    course_teacher_dict = {}
    for c in course_elective+course_required:
        for cl in my_class:
            course_teacher_dict[(c,cl)]=coursedict[c].pop()
    '''
    course_teacher_dict={
        '(语文，一年一班)'：'老师1'，
        '(语文，一年一班)'：'老师1'，
        '(语文，一年一班)'：'老师1'，
        '(语文，一年二班)'：'老师2'，
        ...
    }
    '''
    classsql = "select id,caption from class"
    cur.execute(classsql)
    classobj = cur.fetchall()
    csvfile = open(score_path, 'w')
    writer = csv.writer(csvfile)
    writer.writerow(("id", "test", 'number', 'mycourse_id', 'myteacher_id'))
    id_number = 1
    for cla in classobj:
        #每个班级
        studentsql = "select id, sname, myclass_id from student where myclass_id = %d" % cla[0]
        cur.execute(studentsql)
        studentobj = cur.fetchall()
        print("class %d" % cla[0])
        for stu in studentobj:
            #每个学生
            temp = []
            print("student %s" % stu[1])
            for co in course_required:
                #必修课
                course_id = course_teacher_dict[(co,cla[1])]
                for t in exam_name:
                    tempson = (id_number, t, random.randint(50,100), course_id, stu[0])
                    id_number += 1
                    temp.append(tempson)

            for co in random.sample(course_elective,3):
                course_id = course_teacher_dict[(co, cla[1])]
                for t in exam_name:
                    tempson = (id_number, t, random.randint(50,100), course_id, stu[0])
                    id_number += 1
                    temp.append(tempson)
            writer.writerows(temp)
    csvfile.close()

def create_score(cur):
    coursesql = "select id, cname, myteacher_id from course order by cname"
    cur.execute(coursesql)
    courseobj = cur.fetchall()
    coursedict = {}
    for co in courseobj:
        if co[1] not in coursedict:
            coursedict[co[1]] = [co[0],co[0],co[0]]
        else:
            coursedict[co[1]].append(co[0])
            coursedict[co[1]].append(co[0])
            coursedict[co[1]].append(co[0])
    '''
    coursedict={
        '语文'：[老师1，老师1，老师1，老师2，老师2，老师2]
        ...
    }
    '''
    course_teacher_dict = {}
    for c in course_elective+course_required:
        for cl in my_class:
            course_teacher_dict[(c,cl)]=coursedict[c].pop()
    '''
    course_teacher_dict={
        '(语文，一年一班)'：'老师1'，
        '(语文，一年一班)'：'老师1'，
        '(语文，一年一班)'：'老师1'，
        '(语文，一年二班)'：'老师2'，
        ...
    }
    '''

    classsql = "select id,caption from class"
    cur.execute(classsql)
    classobj = cur.fetchall()
    for cla in classobj:
        #每个班级
        studentsql = "select id, sname, myclass_id from student where myclass_id = %d" % cla[0]
        cur.execute(studentsql)
        studentobj = cur.fetchall()
        print("class %d" % cla[0])

        for stu in studentobj:
            #每个学生
            print("student %s" % stu[1])
            for co in course_required:
                #必修课
                course_id = course_teacher_dict[(co,cla[1])]
                for t in exam_name:
                    sql = """insert into score(mystudent_id, mycourse_id, test,number) values (%d, %d, '%s', %d)
                    """ % (stu[0],course_id,t,random.randint(50,100))
                    try:
                        cur.execute(sql)
                    except Exception as e:
                        print(sql)
                        print(e)
            for co in random.sample(course_elective,3):
                course_id = course_teacher_dict[(co, cla[1])]
                for t in exam_name:
                    sql = """insert into score(mystudent_id, mycourse_id, test,number) values (%d, %d, '%s', %d)
                    """ % (stu[0],course_id,t,random.randint(50,100))
                    try:
                        cur.execute(sql)
                    except Exception as e:
                        print(sql)
                        print(e)

def main1():
    con = connections["default"]
    cur = con.cursor()

    create_teacher(cur)
    create_course(cur)
    create_class(cur)
    create_student(cur)
    create_score(cur)

    if cur:
        cur.close()
    if con:
        con.close()

def main2():
    con = connections["default"]
    cur = con.cursor()

    create_class_csv()
    create_student_csv(cur)
    create_teacher_csv()
    create_cource_csv(cur)
    create_score_csv(cur)

    if cur:
        cur.close()
    if con:
        con.close()

def run():
    import time
    T=time.time()
    try:
        main2()
        print('okkkk')
    except Exception as e:
        print(e)
    print(time.time()-T)


if __name__ == '__main__':
    print("run create_teacher")
    run()
    print("end create_teacher")
