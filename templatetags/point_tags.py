from django import template
register = template.Library()

from django.contrib.contenttypes.models import ContentType

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

@register.inclusion_tag('points/test.html')
def show_google_map(model_instance, css_id="default-map"):
    ''' Turn a DOM element into a map using the google API

    {% show_google_map model_instance css_id%}
    '''
    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id
    if Point.objects.filter(content_type = ct, object_id=obj_id):
        point = Point.objects.filter(content_type = ct, object_id=obj_id)[0]
    else:
        return None

    return locals()

'''
# FIXME? right now I am trying to just be able to {% include ajax_jquery.html %}

@register.inclusion_tag('points/add_form_ajax.html')
def add_point_ajax(css_class):
    '' Add the javascript necessary to ui-dialog the point form

    {% add_point_ajax css_class %}

    ''

    return locals()
'''
