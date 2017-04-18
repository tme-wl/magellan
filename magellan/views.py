from django.shortcuts import render
from django.http import HttpResponse
import hashlib
import requests


def home(request):
    signature = request.GET.get("signature")
    # 'a1d438a9085407772d2c2760d6d0065a28e652fb'
    timestamp = request.GET.get("timestamp")
    # "1492009578"
    nonce = request.GET.get("nonce")
    # "774368487"
    echostr = request.GET.get("echostr")

    token = 'qingsong'
    hashlist = [token, timestamp, nonce]
    hashlist.sort()
    hashstr = ''.join([s for s in hashlist])
    hashstr = hashlib.sha1(hashstr.encode("utf8")).hexdigest()
    if hashstr == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("")



def get_access_token():
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxfd0dfcb741bb8cd5&secret=e5b13f0db3cee4fe2a22024190b82b63"
    return "access_token"


def send_message(request):
    access_token = get_access_token()
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % access_token
    template_id = "sSmVoett8xyRvZGly8-73FZZq_uUk9FHAZw4BbjmofM"
    send_data = {
        "touser": "OPENID",
        "template_id": template_id,
        "topcolor": "#FF0000",
        "data": {
            "username": {
                "value": "王龙",
                "color": "#173177"
            },
            "service": {
                "value": "神威太湖之光",
                "color": "#173177"
            },
            "time": {
                "value": "2017-04-10 12:32:56",
                "color": "#173177"
            }
        }
    }
    requests.post(url, data=send_data)



def home2(request):
    if request.method == 'GET':
        signature = request.GET.get("signature")
        #'a1d438a9085407772d2c2760d6d0065a28e652fb'
        timestamp = request.GET.get("timestamp")
        #"1492009578"
        nonce = request.GET.get("nonce")
        #"774368487"
        echostr = request.GET.get("echostr")

        print(signature,timestamp,nonce,echostr)
        token = 'qingsong'
        hashlist = [token, timestamp, nonce]
        print(hashlist,'adfadsf')
        print(1)
        hashlist.sort()
        print(2)
        hashstr = ''.join([s for s in hashlist])
        print(hashstr,'hashstr')
        print(type(hashstr))
        hashstr = hashlib.sha1(hashstr.encode("utf8")).hexdigest()
        print(4)
        print(hashstr, signature)
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("")


def home1(request):
    try:
        print(request.GET)
        signature = request.GET.get("signature")
        timestamp = request.GET.get("timestamp")
        nonce = request.GET.get("nonce")
        echostr = request.GET.get("echostr")
        token = 'qingsong'
        hashlist = [token, timestamp, nonce]
        print(hashlist,'adfadsf')
        print(1)
        hashlist.sort()
        print(2)
        hashstr = ''.join([s for s in hashlist])
        print(3)
        hashstr = hashlib.sha1(hashstr).hexdigest()
        print(4)
        print(hashstr, signature)
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("")
    except Exception as e:
        print(e)

    #return render(requests,'home.html')