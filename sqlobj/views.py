# coding=utf-8

from django.shortcuts import render
from sqlobj.models import Question, Answer, MyClass, MyStudent, MyTeacher, MyCourse, MyScore
from django.db.models.loading import get_model
from django.http import HttpResponse
from django.db import connections
import json
from django.views.decorators.csrf import csrf_exempt
import time
import logging
from django.template import Context, Template
from common.pagination import Pagination
from django.template.loader import get_template
from django.forms.models import model_to_dict
logger = logging.getLogger("magellan")


# Create your views here.

def ajaxresponse(ret):
    return HttpResponse(content=json.dumps(ret), content_type="application/json")


def get_table_html(request, table_name):
    """
    获取mysql的基本数据表
    :param table_name: 
    :return: 
    """
    forverginkey = ['myclass', 'myteacher', 'mystudent', 'mycourse']
    title_name_obj = get_model('sqlobj', table_name)
    title_name = []
    for field in title_name_obj._meta.fields:
        if field.name in forverginkey:
            field.name = field.name + "_id"
            field.verbose_name = field.verbose_name + "(外键)"
        title_name.append([field.name, field.verbose_name])
    return_data = eval(table_name + ".objects.all()")
    obj = Pagination(request, len(return_data))
    start = obj.start()
    end = obj.end()
    pagination = obj.pagination()
    my_data = []
    for son in return_data[start: end]:
        temp = []
        for name in title_name:
            temp.append(model_to_dict(son).get(name[0]))
        my_data.append(temp)

    msg = {"my_data": my_data, "pagination": pagination, 'title_name': title_name}
    # 获取模板 渲染模板
    template = get_template("show_data.html")
    context = Context(msg)
    html = template.render(context)
    return html


def get_table(request):
    """
    视图函数,演示分页功能,
    reurn_data为所有的数据列表,里面一list形式装载所有数据
    这里演示为从Models里面取出的所有数据
    """
    table_name = request.GET.get("tablename", '')
    if not table_name:
        logger.warning("查询表格的时候没有传入表格名称")
        return ajaxresponse({"table_html": ''})
    return ajaxresponse({"table_html": get_table_html(request, table_name)})


def mysql_practice(request, num=1):
    """获取mysql页面以及基本数据"""
    # 获取数据表格table
    table_html = get_table_html(request, "MyClass")
    myurl = request.path
    urllist = myurl.split('/')
    if urllist[3] == '':
        urllist[3] = 1
    if int(urllist[3]) <= 0:
        urllist[3] = 1
    newurl = '/' + urllist[1] + "/" + urllist[2] + '/' + str(urllist[3]) + '/'
    msg = {"table_html": table_html, 'myurl': newurl}
    # 获取第num题
    msg.update(getquestion(num))
    # msg = {
    #     "table_html"
    #     "myurl"
    #     "question"
    #     "id"
    #     "questionclass"
    # }
    return render(request, "mysql_practice.html", msg)


def addmysql(request):
    if request.method == 'POST':
        return render(request, "addmysql.html")
    else:
        table_html = get_table_html("MyClass")
        return render(request, "addmysql.html", {"table_html": table_html})


def getquestion(num):
    """获取第num题"""
    question_id = int(num)
    if question_id <= 0:
        question_id = 1
    question_obj = Question.objects.order_by('id').last()
    # 有bug
    if not question_obj:
        logger.warning("Question未查到数据")
        return {"question": "", "id": 0, "questionclass": ''}
    if question_obj.number < question_id:
        text = '你刷完所有题目咯。'
        id = question_obj.number
        return {"question": text, "id": id, 'questionclass': 3}
    try:
        obj = Question.objects.get(number=question_id)
        text = obj.text
        id = obj.number
        qclass = obj.qclass
    except:
        text = '对不起，没有这道题。'
        id = 1
        qclass = ''
    finally:
        return {"question": text, "id": id, 'questionclass': qclass}


def get_sql_time(cur, mysql):
    """
    获取mysql语句执行的时间
    若时间短 执行10次 取平均时间
    :param cur: 
    :param mysql: 
    :return: 
    """
    T = time.time()
    cur.execute(mysql)
    answer = cur.fetchall()
    T2 = time.time()
    time_list = [T2 - T]
    if T2 - T < 50:
        for i in range(10):
            T = time.time()
            cur.execute(mysql)
            answer = cur.fetchall()
            T2 = time.time()
            time_list.append(T2 - T)
    return answer, round((sum(time_list) / len(time_list)) * 1000, 2)


@csrf_exempt
def uploadmysql(request):
    con = connections["default"]
    cur = con.cursor()
    questionid = int(request.POST.get('questionid', 0))
    # 题目类型 qclass=1为填空题 2位选择题
    qclass = int(request.POST.get('qclass'), 0)
    if qclass == 1 and questionid:  # sqlyuju
        mysqlstr = request.POST.get('mysql', '')
        if not mysqlstr:
            msg = {"head": "error", 'info': '参数错误'}
        else:
            try:
                obj = Question.objects.get(id=questionid)
                cur.execute(mysqlstr)
                myanswer, usetime = get_sql_time(cur, mysqlstr)
                cur.execute(obj.answersql)
                theanswer = cur.fetchall()
                if theanswer == myanswer:
                    answerobj = Answer.objects.filter(question=questionid)
                    if answerobj:
                        msg = {"head": "ok",
                               "info": "恭喜你答对了,用时%s毫秒,历史最快%s毫秒" % (str(usetime), str(answerobj[0].usetime))}
                        if answerobj[0].usetime > float(usetime):
                            answerobj[0].usetime = float(usetime)
                            answerobj[0].name = '匿名'
                            answerobj[0].save()
                    else:
                        ans = Answer()
                        ans.question = obj
                        ans.sqltext = mysqlstr
                        ans.name = '匿名'
                        ans.usetime = float(usetime)
                        ans.save()
                        msg = {"head": "ok", "info": "恭喜你答对了,用时%s毫秒." % (str(usetime),)}
                else:
                    msg = {"head": "error", 'info': '答案错误'}
            except Exception as e:
                msg = {"head": "error", "info": 'sql错误:' + str(e)}
    elif qclass == 2 and questionid:  # choice
        qchoice = int(request.POST.get('qchoice'), 0)
        try:
            obj = Question.objects.get(id=questionid)
            if qchoice and qchoice == obj.thechoice:
                msg = {'head': 'ok', 'info': '恭喜你答对了'}
            else:
                msg = {'head': 'ok', 'info': '回答错误'}
        except Exception as e:
            msg = {"head": "error", "info": '错误:' + str(e)}
    else:
        msg = {"head": "error", 'info': '参数错误'}
    if cur:
        cur.close()
    if con:
        con.close()
    return ajaxresponse(msg)


def getanswer(request):
    questionid = int(request.GET.get('questionid', 0))
    obj = Question.objects.get(id=questionid)
    msg = {"html": obj.answersql, 'qclass': obj.qclass, 'qchoice': obj.thechoice}
    return ajaxresponse(msg)


def test(request):
    return render(request, 'test.html')
