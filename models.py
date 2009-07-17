from django.contrib.gis.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic



class Point(models.Model):
    ''' a geographic point that can be added to any model instance

    '''
    zoom = models.PositiveIntegerField(blank=True, null=True)
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

