=============
django-points
=============

A reusable app for tagging 1 or more geographic location to any model instance.

Building for pinax-compliance and convenient JSON API.

Installation
  * put the dir on your pythonpath
  * add 'points' to INSTALLED_APPS
  * syncdb
  * makes sure that your site_name is correct in the db
  * put (r'^points/', include('points.urls')), in main urlconf
    # FIXME?
    * you may use a different location but get_absolute_urls are
      directed here



