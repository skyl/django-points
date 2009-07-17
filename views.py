from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType


from points.forms import PointForm
from points.models import Point

#from vectorformats.Formats import Django, GeoJSON
from django.core import serializers


def all(request):
    points = Point.objects.all()

    if request.is_ajax():
        return HttpResponse(serializers.serialize("json",points),\
                mimetype='application/javascript')

    else:
        context = {'points':points, }
        return render_to_response('points/all.html', context,\
                context_instance=RequestContext(request))

def detail(request, id):
    ''' Responds with the point and related object information

    '''

    try:
        point = Point.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse('points_list'))

    t = ContentType.objects.get(\
            app_label = point.content_type.app_label,
            model = point.content_type.model)

    o = t.get_object_for_this_type(id = point.object_id)

    context = {'point':point, 'object':o , }

    if request.is_ajax():
        return HttpResponse(serializers.serialize("json", point),
                mimetype='application/javascript')

    else:
        return render_to_response('points/detail.html', context,\
                context_instance=RequestContext(request))

@login_required
def delete(request, id):
    ''' can delete a point with a POST from the owner via ajax or otherwise

    '''
    try:
        point = Point.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse('points_list'))

    context = {'point':point,}
    if request.user == point.owner:

        if request.method == 'POST':
            if request.is_ajax():
                point.delete()
                return HttpResponse(status=201)

            else:
                point.delete()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

        else:
            return render_to_response('points/confirm_delete.html', context,\
                    context_instance=RequestContext(request))

    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def form(request, id):
    ''' Change the point location for a Point '''

    try:
        point = Point.objects.get(id=id)
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if request.method == 'POST' and point.owner == request.user:

        form = PointForm(request.POST, instance=point)

        if form.is_valid():
            if request.is_ajax():
                form.save()
                return HttpResponse(status=201)
            else:
                form.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER']) 

    elif point.owner == request.user:
        form = PointForm( instance=point )
        context = {'point':point, 'form':form}
        return render_to_response('points/change.html', context,\
                context_instance=RequestContext(request) )

    else:
        return HttpResponseRedirect(request.META['HTTP_REFERAL'])
'''

Below is scratch, not documentation.

    one can supply id-only to change an existing Point or, alter
    print request.META['HTTP_REFERER']

    if id and not app_label and not model_name and not slug:
        if request.method == 'POST':
            try:
                point = Point.objects.get(id=id)
            except:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if request.method == 'POST':
        if point:
            form = PointForm(request.POST, instance = point)
        else:
            form = PointForm(request.POST)

        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse(status=201)
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

    else:
        if point:
            context = {'point':point,}
        else:
            context = {}

        return render_to_response('points/point_form.html', context,\
                context_instance = RequestContext(request) )
'''
