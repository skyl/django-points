from django import template
register = template.Library()

from django.contrib.contenttypes.models import ContentType
from olwidget.widgets import MapDisplay

from points.models import Point

@register.inclusion_tag('points/link.html')
def add_point_link(model_instance, css_class="add-point"):
    '''Inclusion tag to rendering simple link to the point form page

    arguments: model_instance, css_class
    {% add_point_link model_instance css_class %}
    '''
    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()

@register.inclusion_tag('points/show_google_map.html')
def show_google_map(model_instance, css_id="default-map"):
    ''' Turn a DOM element into a map using the google API

    {% show_google_map model_instance css_id%}
    Note that this returns the *latest* point that has been
    added to the model instance.
    '''
    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    if Point.objects.filter(content_type = ct, object_id=obj_id):
        point = Point.objects.filter(content_type = ct, object_id=obj_id)[0]
    else:
        return None

    return locals()

@register.inclusion_tag('points/show_ol_map.html')
def show_ol_map(model_instance):
    ''' Takes a model instance and returns display of all points html

    {% show_ol_map model_instance %}
    '''
    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    points = Point.objects.filter(content_type = ct, object_id=obj_id)

    map = MapDisplay( fields=[p.point for p in points],
            map_options = {
                    'map_style':{'width':'240px', 'height':'160px',},
                    'layers': ['osm.mapnik','google.hybrid'],
            }
    )


    return locals()

@register.inclusion_tag('points/show_ol_media.html')
def show_ol_media(model_instance):
    ''' What needs to be in head for show_ol_map tag

    '''
    r = show_ol_map(model_instance)
    return r
