from django.conf.urls import url
from . import views

app_name = 'attendance'
urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^attendancerecord/list/$', views.attendance_record_list,
        name='attendance/attendancerecord/list'),
]
