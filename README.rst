=============
django-points
=============

A reusable app for tagging 1 or more geographic location to any model instance.

Building for pinax-compliance and flexible, powerful API.

Installation
------------
  * check out the source as points (rather than django-points)
    alternately, just mv the directory.
  * put the dir on your pythonpath
  * add 'points' to INSTALLED_APPS
  * add "points.context_processors.ol_media" to your context_procs in settings
    alternately, add the context processor on a perview basis.
  * syncdb
  * makes sure that your site_name is correct in the db
  * put (r'^points/', include('points.urls')), in main urlconf

Requirements
------------
  * olwidget
  * django.contrib.contenttypes (installed by default)
  * GeoDjango with geoip #FIXME make optional?
    http://geolite.maxmind.com/download/geoip/api/c/

  Note::

    This app is only tested with postgresql_psycopg2


Usage
-----
    
    You now have access to the following urls:

        url(r'^$', view='points.views.list', name="points_list"),
        
        url(r'^(?P<id>\d+)/$', view='points.views.detail', name='points_detail'),

        url(r'^delete/(?P<id>\d+)/', view='points.views.delete', name='points_delete'),

        url(r'change/(?P<id>\d+)/', view='points.views.change', name='points_change'),

        url(r'list/(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<id>\d+)/$', view='points.views.list', name='points_list'),

        url(r'list/(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/$', view='points.views.list', name='points_list'),

        url(r'add/(?P<app_label>[-\w]+)/(?P<model_name>[-\w]+)/(?P<id>\d+)/$', view='points.views.add', name='points_add'),

    
  **Note for pinax users and those using django-uni-form**
  This css rule must be removed from uni-form-generic.css (or over-ridden)
  for the open layers form widget to work (olwidget).

	    .uniForm .inlineLabels label,
	    .uniform .inlineLabels .label{ float: left; margin: 0; padding: 0; line-height: 100%; position: relative; }

  Alternately, you may set the rule:
            
            div#id_point_map { clear:both; }


  there may be a bug in YOUR env,
  psycopg2, Pinax that may cause an error when running syncdb::

    psycopg2.ProgrammingError: column points_point.point does not exist

  Don't fret, run::

    $ ./manage.py sqlall

  Get the output of this into your database shell.
	


