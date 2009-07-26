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


'''
# FIXME? right now I am trying to just be able to {% include ajax_jquery.html %}

@register.inclusion_tag('points/add_form_ajax.html')
def add_point_ajax(css_class):
    '' Add the javascript necessary to ui-dialog the point form

    {% add_point_ajax css_class %}

    ''

    return locals()
'''
