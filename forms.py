from django import forms
from olwidget.widgets import OLWidget
from points.models import Point


# FIXME I want to center the map for the form
# based on the GeoIP ... I think that I need to override
# __init__
# http://www.djangosnippets.org/snippets/26/
# http://geodjango.org/docs/geoip.html
#
#from django.contrib.gis.utils import GeoIP

#>>> g = GeoIP()
#>>> g.country('google.com')
#{'country_code': 'US', 'country_name': 'United States'}
#>>> g.city('72.14.207.99')
#{'area_code': 650,
#'city': 'Mountain View',
#'country_code': 'US',
#'country_code3': 'USA',
#'country_name': 'United States',
#'dma_code': 807,
#'latitude': 37.419200897216797,
#'longitude': -122.05740356445312,
#'postal_code': '94043',
#'region': 'CA'}
#>>> g.lat_lon('salon.com')
#(37.789798736572266, -122.39420318603516)
#>>> g.lon_lat('uh.edu')
#(-95.415199279785156, 29.77549934387207)
#>>> g.geos('24.124.1.80').wkt
#'POINT (-95.2087020874023438 39.0392990112304688)'

#ip = request.META['REMOTE_ADDR']
# can be a tuple if proxied!


class PointForm(forms.ModelForm):
    ''' Can take a request object to center the map

    '''

    point = forms.CharField(widget=OLWidget(
            # the following parameters do not affect the jq-ui forms
            # they must be set directly in jqueryui_add_form.html
            map_options = {
                    'default_zoom':1,
                    #'layers': ['google.hybrid',],
                    'map_style': {
                        'width':'100%',
                        'height':'550px',
                    },
                    #'default_lon':g.lat_lon[1],
                    #'default_lat':g.lat_lon[0],
            }
    ))

    class Media:
        css = {
                'all': (
                    'points/css/points.css',
                    'points/css/jq-ui.css',
                )
        }

        js = ('points/js/points.js',)

    class Meta:
        model = Point

