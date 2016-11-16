'''
Created on 16 nov. 2016

@author: Hugo
'''
from django.conf.urls import url
from . import views

app_name = 'attendance'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
]
