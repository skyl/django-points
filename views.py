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


def list(request, app_label=None, model_name=None, id=None):
    ''' List all points (ALL, all for model instance, or all for table)

    I wanted to overload a view for fun so as to be more dry but all of this
    logic might be wetter still FIXME?
    '''

    if not id and not model_name and not app_label:
        points = Point.objects.all()
        context = { 'points':points, }

    elif id and model_name and app_label:
        try:
            ct = ContentType.objects.get(\
                    app_label = app_label,
                    model = model_name)

            obj = ct.get_object_for_this_type( id=id )

            points = Point.objects.filter( content_object=obj )

        except:
            # FIXME, does this look good?  In need of a convention...
            if request.is_ajax():
                return HttpResponse(status=500)
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

        points = Point.objects.filter(content_object = obj)
        context = {'points':points, 'object':obj, 'content_type':ct, }

    elif app_label and model_name and not id:
        try:
            ct = ContentType.objects.get(\
                    app_label = point.content_type.app_label,
                    model = point.content_type.model)
        except:
            # FIXME, does this look good?  In need of a convention...
            # and, this could be a bit more DRY?
            if request.is_ajax():
                return HttpResponse(status=500)
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

        points = Point.objects.filter(content_type = ct)
        context = {'points':points, 'content_type':ct, }

    else:
        # FIXME seriously, this might not be cool..
        if request.is_ajax():
            return HttpResponse(status=500)

        else:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])


    if request.is_ajax():
        return HttpResponse(serializers.serialize("json",points),\
                mimetype='application/javascript')

    else:
        return render_to_response('points/all.html', context,\
                context_instance=RequestContext(request))

def detail(request, id):
    ''' Responds with the point and related object information

    '''

    try:
        point = Point.objects.get(id=id)

    except:
        return HttpResponseRedirect(reverse('points_list'))

    ct = ContentType.objects.get(\
            app_label = point.content_type.app_label,
            model = point.content_type.model)

    obj = ct.get_object_for_this_type(id = point.object_id)

    context = {'point':point, 'object':obj, 'content_type': ct,  }

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
        # FIXME?
        if request.is_ajax():
            return HttpResponse(status=500)

        else:
            #return HttpResponseRedirect(reverse('points_list'))
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

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
def change(request, id):
    ''' Change the data for a single Point() obj '''

    try:
        point = Point.objects.get(id=id)
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if request.method == 'POST' and point.owner == request.user:

        # FIXME? What needs to be posted with ajax to make a valid form?
        # I would hope that you could just post 1 field and the others
        # would stay the same.  Think that is the way that it would work.
        form = PointForm(request.POST, instance=point)

        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse(status=201)
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

    elif point.owner == request.user:
        form = PointForm( instance=point )
        context = {'point':point, 'form':form, }
        return render_to_response('points/change.html', context,\
                context_instance=RequestContext(request) )

    else:
        return HttpResponseRedirect(request.META['HTTP_REFERAL'])

@login_required
def add(request, app_label, model_name, id):
    '''add a point to a content_object

    POST the point and the zoom.  The owner is request.user and the related
    obj is received from the url.
    '''
    try:
        ct = ContentType.objects.get(\
                app_label = app_label,
                model = model_name)
        obj = ct.get_object_for_this_type( id=id )

    except:
        if request.is_ajax():
            # FIXME? is this the right thing to return?
            return HttpResponse(status=500)

        else:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if request.method == 'POST':
        request.POST.update( {'owner':request.user.id, 'object_id':id,\
                'content_type':ct.id, 'content_obj':obj,} )
        form = PointForm(request.POST)

        if form.is_valid():
            form.save()

            # FIXME? is this really a way that we can handle the redirect?
            if request.is_ajax():
                return HttpResponse(status=201)

            else:
                try:
                    return HttpResponseRedirect(obj.get_absolute_url())
                except:
                    # FIXME, where am I going with this?
                    return HttpResponseRedirect('/')

    else:
        form = PointForm()

    context = {'form':form, 'object':obj, 'content_type':ct, }

    return render_to_response('points/add.html', context,\
            context_instance = RequestContext(request))


