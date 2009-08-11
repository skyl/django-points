
Requirements
============

* GeoDjango
* olwidget
* pinax 0.7b3 or later
* jQuery and jQuery-UI

Installation
============

settings
--------

  * put 'points' into INSTALLED_APPS
  * add to context processors::

    'points.context_processors.ol_media',
    'points.context_processors.GAK',

  * Get http://code.google.com/apis/maps/signup.html a GOOGLE_MAPS_API key and add it to settings::

    GOOGLE_API_KEY = ...

  * syncdb

urls
----

  * add to your url patterns::

    (r'^points/', include('points.urls')),

QuickStart
==========

* At the top of the template::

  {% load point_tags %}

* In head you could put::

  {% include 'points/jqueryui_add_form.html' %}
  {% show_google_map model_instance "map-id" %}

* In body, where you would like the link to the form widget to go::

  {% add_point_link model_instance %}

* Where you would like the map to go you might put::
  
  <div id="map-id" style="width:45%; height:200px; float:right;"></div>

For more information check docs/api.rst; there are many more options and tags.


