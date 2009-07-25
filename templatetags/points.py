from django import template

register = template.Library()


@register.inclusion_tag('points/link.html')
def add_point_link(model_instance, css_class=None):
    '''Inclusion tag to rendering simple link to the point form page

    arguments: model_instance, css_class
    {% add_point_link model_instance css_class %}
    '''
    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()
