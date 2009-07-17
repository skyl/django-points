from django.contrib.gis.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic



class Point(models.Model):
    ''' a geographic point that can be added to any model instance

    '''
    zoom = models.PositiveIntegerField(blank=True, null=True)
    point = models.PointField()
    objects = models.GeoManager()

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return "%s-%s" % (self.content_object, self.point)



