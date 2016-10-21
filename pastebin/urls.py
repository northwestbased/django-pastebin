from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getpaste/([\da-zA-Z]+)$', views.getpaste, name='getpaste'),
    url(r'^paste$', views.paste, name='paste'),
    url(r'^([\da-zA-Z]+)$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
    url(r'^([\da-zA-Z]+)/createcomment$', views.createcomment, name='createcomment')
]
