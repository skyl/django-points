from django.contrib.gis.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Point(models.Model):
    ''' a geographic point that can be added to any model instance

    '''
    zoom = models.PositiveIntegerField(blank=True, null=True)
    datetime = models.DateTimeField(editable=False, auto_now=True)
    point = models.PointField()
    objects = models.GeoManager()

    owner = models.ForeignKey('auth.User')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return "%s-%s" % (self.content_object, self.point)

    @models.permalink
    def get_absolute_url(self):
        return ('points.views.detail', str(self.id))

    class Meta:
        ordering=( '-datetime', )

def get_point_for_object(obj):
    ''' takes an object and gets the last point that was add to it.

    '''
    ct = ContentType.objects.get_for_model(obj)
    id = obj.id
    return Point.objects.filter( content_type=ct, object_id=id )[0]

