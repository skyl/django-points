from django.contrib.gis.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Point(models.Model):
    ''' a geographic point that can be added to any model instance

    '''
    zoom = models.PositiveIntegerField(blank=True, null=True, help_text="""Where
            is this""")
    datetime = models.DateTimeField(editable=False, auto_now=True)
    # FIXME where is the help text? I might have to just append the help-text
    # with javascript or have a help pop-up alert or something.
    point = models.PointField(help_text='''
            Choose the hand to drag the map;
            double-click to center and zoom.
            Choose the pencil to place a point.
            If there are more layers installed,
            you may choose them by clicking the plus button on the right.
    ''')
    objects = models.GeoManager()

    owner = models.ForeignKey('auth.User')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return "%s-%s" % (self.content_object, self.point)

    @models.permalink
    def get_absolute_url(self):
        return ('points.views.detail', (str(self.id),))

    class Meta:
        ordering=( '-datetime', )

def get_point_for_object(obj):
    ''' takes an object and gets the last point that was add to it.

    '''
    ct = ContentType.objects.get_for_model(obj)
    id = obj.id
    return Point.objects.filter( content_type=ct, object_id=id )[0]

