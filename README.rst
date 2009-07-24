=============
django-points
=============

A reusable app for tagging 1 or more geographic location to any model instance.

Building for pinax-compliance and convenient JSON API.

Installation
  * check out the source as points (rather than django-point)
    alternately, just mv the directory.
  * put the dir on your pythonpath
  * add 'points' to INSTALLED_APPS
  * syncdb
  * makes sure that your site_name is correct in the db
  * put (r'^points/', include('points.urls')), in main urlconf
  * requires olwidget and django.contrib.contenttypes (installed by default)
    in addition to GeoDjango.

  Note::

    This app is only tested with postgresql_psycopg2


  **Note for pinax users and those using django-uni-form**
  This css rule must be removed from uni-form-generic.css (or over-ridden)
  for the open layers form widget to work (olwidget).

	    .uniForm .inlineLabels label,
	    .uniform .inlineLabels .label{ float: left; margin: 0; padding: 0; line-height: 100%; position: relative; }


  pro-tip: there may be a bug in one of: Django, Geodjango,
  psycopg2, Pinax that may cause and error on syncdb::

    psycopg2.ProgrammingError: column points_point.point does not exist

  Don't fret, run::

    $ ./manage.py sqlall

  Get the output of this into your database shell.
	


