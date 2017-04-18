from django.conf.urls import patterns, include, url

urlpatterns = patterns('login',
    url(r'^login/$', 'views.login'),
    url(r'^register/$', 'views.register'),
    url(r'retrievet/$', 'views.retrievet'),
    )