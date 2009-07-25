from django import forms
from olwidget.widgets import OLWidget
from points.models import Point

#from django.contrib.gis.utils import GeoIP

class PointForm(forms.ModelForm):
    ''' Can take a request object to center the map

    '''

    point = forms.CharField(widget=OLWidget(
        map_options = {}
    ))

    class Meta:
        model = Point

