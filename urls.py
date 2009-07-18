from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

urlpatterns = patterns('',
    url(r'^$', view='points.views.list', name="points_list"),
    url(r'^(?P<id>\d+)/$', view='points.views.detail', name='points_detail'),

    url(r'^delete/(?P<id>\d+)/', view='points.views.delete', name='points_delete'),

    url(r'change/(?P<id>\d+)/', view='points.views.change', name='points_change'),


    url(r'list/(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<id>\d+)/$',\
            view='points.views.list', name='points_list'),

    url(r'list/(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/$',\
            view='points.views.list', name='points_list'),

    url(r'add/(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<id>\d+)/$',\
            view='points.views.add', name='points_add'),

)
