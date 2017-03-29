from django.conf.urls import patterns, include, url

urlpatterns = patterns('sqlobj',
    url(r'^mysqlpractice/(?P<num>[0-9]+)/$', 'views.mysqlpractice'),
    url(r'^mysqlpractice/$', 'views.mysqlpractice'),
    url(r'^gettable/$', 'views.get_table'),
    url(r'^addmysql/$', 'views.addmysql'),
    url(r'^getquestion/$', 'views.getquestion'),
    url(r'^uploadmysql/$', 'views.uploadmysql'),
    url(r'^getanswer/$', 'views.getanswer'),
    url(r'^test/$', 'views.test'),
    )