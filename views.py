from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

from points.forms import PointForm
from points.models import Point

from vectorformats.Formats import Django, GeoJSON
'''
>>> qs = Model.objects.filter(city="Cambridge")
>>> djf = Django.Django(geodjango="geometry", properties=['city', 'state'])
>>> geoj = GeoJSON.GeoJSON()
>>> string = geoj.encode(djf.decode(qs))
>>> print string
'''

from django.core import serializers


def all(request):
    points = Point.objects.all()
    djf = Django.Django(geodjango="point",\
            properties=['content_object'])
    geoj = GeoJSON.GeoJSON()

    #if request.is_ajax():
    if True:
        response_dict = {'points':points,}
        return HttpResponse(serializers.serialize("json",points),\
                mimetype='application/javascript')
    else:
        context = {'points':points, }
        return render_to_response('points/all.html', context,\
                context_instance=RequestContext(request))

'''
@login_required
def point_form(request, model=None, slug=None, id=None):
    print request.META['HTTP_REFERER']

    if id:
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

def point_show(request, id):
    point = Point.objects.get(id=id)
    context = {'point':point,}
    return render_to_response('points/point_display.html', context,\
                context_instance = RequestContext(request) )
'''
