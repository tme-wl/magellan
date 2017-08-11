from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    return render(requests,'home.html')