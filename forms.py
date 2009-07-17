from django import forms
from olwidget.widgets import OLWidget
from points.models import Point

class PointForm(forms.ModelForm):
    point = forms.CharField(widget=OLWidget())

    class Meta:
        model = Point

