from django.conf.urls import patterns, include, url
from sqlobj import views

urlpatterns = patterns('sqlobj',
    url(r'^mysqlpractice/(?P<num>[0-9]+)/$', views.mysql_practice),
    url(r'^mysqlpractice/$', views.mysql_practice),
    url(r'^gettable/$', views.get_table),
    url(r'^addmysql/$', views.addmysql),
    url(r'^getquestion/$', views.getquestion),
    url(r'^uploadmysql/$', views.uploadmysql),
    url(r'^getanswer/$', views.getanswer),
    url(r'^test/$', views.test),
    )