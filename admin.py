from points.models import Point
from olwidget import admin

admin.site.register(Point, admin.custom_geo_admin(
    {'layers':['google.hybrid'],}))
