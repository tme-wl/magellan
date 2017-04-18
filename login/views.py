from django.shortcuts import render

# Create your views here.

def login(requests):
    return render(requests,'login.html')


def register(requests):
    return render(requests,'register.html')


def retrievet(requests):
    return render(requests,'retrievet.html')


def myhome(requests):
    return render(requests, 'myhome.html')


def changepw(requests):
    return render(requests, 'changepw.html')