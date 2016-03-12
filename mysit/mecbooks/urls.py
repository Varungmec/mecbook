from django.conf.urls import patterns,url

from mecbooks import views

urlpatterns = patterns('',url(r'^$', views.index, name='index'),)