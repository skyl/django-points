from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

urlpatterns = patterns('',
    url(r'^$', view='points.views.all', name="point_list"),
    url(r'(?P<id>\d+)/$', view='points.views.detail', name='point_detail'),

    # FIXME if the slug is just numbers this would be bad
    #url(r'(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<id>\d+)/$',\
    #            view='point_list', name='point_list'),

    #url(r'(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<slug>[-\w]+)/$',\
    #            view='point_list', name='point_list'),

    #url(r'(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/$',\
    #            view='point_list', name='point_list'),



    #url(r'(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<id>\d+)/add/$',\
    #            view='point_form', name='point_form'),
    #url(r'(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<slug>[-\w]+)/add/$',\
    #             view='point_form', name='point_form'),

    #url(r'change/(?P<id>[-\w]+)/', view='point_form', name='point_change'),
    #url(r'delete/(?P<id>[-\w]+)/', view='point_delete', name='point_delete'),




    #url(r'^terms/$', direct_to_template, {"template": "about/terms.html"}, name="terms"),
    #url(r'^privacy/$', direct_to_template, {"template": "about/privacy.html"}, name="privacy"),
    #url(r'^dmca/$', direct_to_template, {"template": "about/dmca.html"}, name="dmca"),
    #url(r'^what_next/$', direct_to_template, {"template": "about/what_next.html"}, name="what_next"),
)
