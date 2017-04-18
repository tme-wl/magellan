from django.shortcuts import render
from sqlobj.models import *
from django.db.models.loading import get_model
from django.http import HttpResponse
from django.db import connections
import json
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.

def ajaxresponse(ret):
    return HttpResponse(content=json.dumps(ret), content_type="application/json")

def get_table_html(table_name):
    forverginkey = ['myclass','myteacher','mystudent','mycourse']
    title_name_obj = get_model('sqlobj', table_name)
    title_name=[]
    for field in title_name_obj._meta.fields:
        if field.name in forverginkey:
            field.name = field.name + "_id"
            field.verbose_name = field.verbose_name + "(外键)"
        title_name.append([field.name, field.verbose_name])
    table_thead_son1 = ""
    table_thead_son2 = ""
    for son in title_name:
        table_thead_son1 += "<th>%s</th>" % son[0]
    for son in title_name:
        table_thead_son2 += "<th>%s</th>" % son[1]
    table_thead_html = "<thead><tr>%s</tr><tr>%s</tr></thead>" % (table_thead_son2,table_thead_son1)

    obj = eval(table_name + ".objects.all()[:30]")
    html_tbody = ""
    for son in obj:
        html_son = ""
        for i in title_name:
            html_son += "<td>%s</td>" % getattr(son, i[0])
        html_tbody += "<tr>%s</tr>" % html_son
    html_son = ""
    for i in title_name:
        html_son += "<td>...</td>"
    html_tbody += "<tr>%s</tr>" % html_son
    return table_thead_html + "<tbody>%s</tbody>" % html_tbody


def get_table(request):
    tablename = request.GET.get("tablename", '')
    return ajaxresponse({"table_html": get_table_html(tablename)})


def mysqlpractice(request, num=1):
    table_html = get_table_html("MyClass")
    myurl = request.path
    urllist = myurl.split('/')
    if urllist[3] == '':
        urllist[3]=1
    if int(urllist[3]) <= 0:
        urllist[3] = 1
    newurl = '/' + urllist[1]+"/"+urllist[2]+'/'+str(urllist[3]) + '/'
    msg={"table_html":table_html,'myurl':newurl}
    msg.update(getquestion(num))
    return render (request,"mysqlpractice.html",msg)


def addmysql(request):
    if request.method == 'POST':
        return render (request, "addmysql.html")
    else:
        table_html = get_table_html("MyClass")
        return render (request, "addmysql.html",{"table_html":table_html})


def getquestion(num):
    question_id = int(num)
    if question_id <= 0:
        question_id = 1
    Questionobj = Question.objects.order_by('id').last()
    #有bug
    if Questionobj.id < question_id:
        text = '你刷完所有题目咯。'
        id = Questionobj.id
        return {"question": text, "id": id, 'questionclass':3}
    try:
        obj = Question.objects.get(id = question_id)
        text = obj.text
        id = obj.id
        qclass = obj.qclass
    except:
        text = '对不起，没有这道题。'
        id = 1
        qclass = ''
    finally:
        return {"question": text, "id":id, 'questionclass':qclass}


def get_sql_time(cur,mysql):
    T = time.time()
    cur.execute(mysql)
    answer = cur.fetchall()
    T2 = time.time()
    time_list = [T2-T]
    if T2-T < 50:
        for i in range(10):
            T = time.time()
            cur.execute(mysql)
            answer = cur.fetchall()
            T2 = time.time()
            time_list.append(T2-T)
    return answer, round((sum(time_list)/len(time_list))*1000,2)


@csrf_exempt
def uploadmysql(request):
    con = connections["default"]
    cur = con.cursor()
    questionid = int(request.POST.get('questionid', 0))
    print(questionid)
    qclass = int(request.POST.get('qclass'), 0)
    if qclass ==1 and questionid:   #sqlyuju
        print(1)
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
                        msg = {"head": "ok", "info": "恭喜你答对了,用时%s毫秒,历史最快%s毫秒" % (str(usetime), str(answerobj[0].usetime))}
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
    elif qclass == 2 and questionid:  #choice
        print(2)
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
        print(3)
        msg = {"head": "error", 'info': '参数错误'}
    if cur:
        cur.close()
    if con:
        con.close()
    return ajaxresponse(msg)


def getanswer(request):
    questionid = int(request.GET.get('questionid', 0))
    obj = Question.objects.get(id=questionid)
    msg = {"html":obj.answersql,'qclass':obj.qclass,'qchoice':obj.thechoice}
    return ajaxresponse(msg)

def test(request):
    return render(request,'test.html')
