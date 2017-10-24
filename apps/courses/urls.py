from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    #url(r'^courses(?P<course_id>\d+)/edit$', views.edit),
    url(r'^courses/(?P<course_id>\d+)/confirm$', views.edit),
    url(r'^courses/(?P<course_id>\d+)/bleh$', views.destroy)
] 