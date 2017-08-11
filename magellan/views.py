from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    print('in home')
    return HttpResponse('okkk')
    # return render(requests, 'home.html')