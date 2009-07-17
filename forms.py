from django import forms
from olwidget.widgets import OLWidget

class PointForm(forms.ModelForm):
    point = forms.CharField(widget=OLWidget())

