from django.contrib.auth.decorators import login_required
import re

from piston.handler import BaseHandler
from piston.utils import rc, throttle

from points.models import Point
from points.forms import PointForm

class PointHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE')
    fields = ('point', 'zoom', 'owner', 'datetime', 'content_type', 'object_id', 'content_object')
    exclude = ('id', re.compile(r'^private_'))
    model = Point

    def read(self, request, id):
        point = Point.objects.get(id=id)
        return point


    def update(self, request, id):
        point = Point.objects.get(id=id)

        # ?? will this work?
        p = PointForm(request.PUT, instance=point)
        p.save()

        return p

    def create(self, request):
        p = PointForm(request.POST)
        p.save()

    def delete(self, request, id):
        point = Point.objects.get(point=point)

        if not request.user == point.owner:
            return rc.FORBIDDEN # returns HTTP 401

        point.delete()

        return rc.DELETED # returns HTTP 204


