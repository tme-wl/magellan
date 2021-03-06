# coding=utf-8

"""magellan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from magellan import views
from sqlobj import views as sqlviews

# # -*- coding: utf-8 -*-
# import xadmin
# xadmin.autodiscover()
#
# # version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sqlobj/', include("sqlobj.urls")),
    url(r'^mylogin/', include('login.urls')),
    # url(r'^$', sqlviews.mysql_practice),
    url(r'^$', views.home),
    # url('^', include('django.contrib.auth.urls')),
    # url(r'xadmin/', include(xadmin.site.urls)),

]



