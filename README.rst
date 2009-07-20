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

  **Note for pinax users and those using django-uni-form**
  This css rule when rendering \{\{form\|as_uni_form\}\}::

	    .uniForm .inlineLabels label,
	    .uniform .inlineLabels .label{ float: left; margin: 0; padding: 0; line-height: 100%; position: relative; }

  Must be removed from uni-form-generic.css (or over-ridden)
  for the open layers form widget to work (olwidget).


	


