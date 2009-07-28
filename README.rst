=============
django-points
=============

A reusable app for tagging geographic location(s) to any model instance.

Building for pinax-compliance, reusability, abstraction.

Installation
------------
    * check out the source as points (rather than django-points)
      alternately, just mv the directory.
    * put the dir on your pythonpath
    * add 'points' to INSTALLED_APPS
    * add "points.context_processors.ol_media" to your context_procs in settings
      alternately, add the context processor on a perview basis.
    * (optional) add "points.context_processors.GAK" to your context_procs, this will provide your
      template (see GOOGLE_API_KEY below) with a {{GAK}} variable for you jsapi key.

    * syncdb
    * makes sure that your site_name is correct in the db
    * put (r'^points/', include('points.urls')), in main urlconf
    * (optional) add
      GOOGLE_API_KEY = 
      'ABQIAAAABH87p-yQOJj-sh06NusQiRTpH3CbXHjuCVmaTc5MkkU4wO1RRhTdrjDBgVDitkd2sidQwpIj12NE2w'
      to your settings.py to use the GOOGLE_MAPS_API for 127.0.0.1:8000 or get your own:
      http://code.google.com/apis/maps/signup.html
      Actually, legally, go read and click their terms if you want to use their service.

Requirements
------------
    * olwidget
    * django.contrib: contenttypes, auth (installed by default) more?
    * django-uni-form for default implementation (some simple hacking
      could remove this as a requirement)::

            $grep -r as_uni_form *

      to find where this is used.
    * GeoDjango
    * jQuery and jq-ui must be on the page to use the current
      "ajax" implementation

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

You can add a link to the "points_add" for any model instance using the add_point_link inclusion tag::

    {% load point_tags %}
    {% add_point_link model_instance css_class %}

Additionally, if you have jQuery and jq-ui on the page you may (in the head of your html document)::

    {% include 'points/jqueryui_add_form.html' %}

Now, instead of requesting the points_add form url,
clicking on the rendered link will give a jquery-ui dialog to the form widget.

Open Layers
+++++++++++

To display a simple olwidget street map
with all of the points that are attached to a certain model instance object
pass that model instance to show_ol_media in <head> and 
show_ol_map where you would like to place the map in the body.

Somewhere near the top of the document::

    {% load point_tags %}

In head::

    {% show_ol_media model_instance %}

To place the map in the body::

    {% show_ol_map model_instance %}

There will be more options to pass to these such as height and width.  
Currently, these are easy to change by hacking the map attr of point_tags.show_ol_map

Help me implement some event-handlers!


Google
++++++

If you would like more layers in the dialog widget form you can add to the layers list in::

    jqueryui_add_form.html

For instance, you could apply::

    "layers": ["google.hybrid", "osm.mapnik"],

With that you should default to google.hybrid and have the choice of open street maps.

To show the latest map tagged to an object you will need the following on you page in the order

Don't forget::

    {% load point_tags %}

In head::

    <script src="http://www.google.com/jsapi?key={{GAK}}" type="text/javascript"></script>
    {% show_google_map model_instance "css_id" %}

In body::

    <div id="css_id" style="width:CHOOSE; height:CHOOSE;"></div>

{% load point_tags %} gives you access to the tag, show_google_map.

  * The google jsapi must be present on the page with the key (see installation)
  * model_instance is the instance that you want to tag such as "tribe" or "topic" or "user".
  * css_id is a string, the id of the DOM element that will contain the map.
  * Then, in the body we place the map div with our desired width and height
  * other style may be added here or factored out into a stylesheet.
  * Other strategies such as creating the div with javascript are possible.

Issues
------

css and javascript
++++++++++++++++++

**Note for pinax users and those using django-uni-form**
This css rule must be removed from uni-form-generic.css (or over-ridden)
for the open layers form widget to work (olwidget).

    .uniForm .inlineLabels label,
    .uniform .inlineLabels .label{ float: left; margin: 0; padding: 0; line-height: 100%; position: relative; }

Alternately, you may set the rule::
            
    div#id_point_map { clear:both; }

Still, the jq-ui map widget is not perfect.  On epiphany, setting a marker down is skewed to the right a tad;
My FF does it right for the first dialog that is opened and then is skewed for the 2,4 and 6th times it seems.

database
++++++++

there may be a bug in your env,
psycopg2, Pinax that may cause an error when running syncdb::

    psycopg2.ProgrammingError: column points_point.point does not exist

Don't fret, run::

    $ ./manage.py sqlall

Get the output of this into your database shell.	
