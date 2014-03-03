# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin
from gmapi import maps

MAP_TYPES =[
    (u'1', _(u"Hybrid")),
    (u'2', _(u"Road map")),
    (u'3', _(u"Satellite")),
    (u'4', _(u"Terrain")),

]
TO_MAPS_OBJ = {
    u'1': maps.MapTypeId.HYBRID,
    u'2': maps.MapTypeId.ROADMAP,
    u'3': maps.MapTypeId.SATELLITE,
    u'4': maps.MapTypeId.TERRAIN,
}

class GMap(models.Model):
    language = models.CharField(_("Language"), max_length=15, choices=settings.LANGUAGES)
    center_lat = models.DecimalField(_("Latitude"), decimal_places=6, max_digits=9)
    center_long = models.DecimalField(_("Longitude"), decimal_places=6, max_digits=9)
    zoom = models.IntegerField(_("Zoom"), max_length=1)
    map_type = models.CharField(_("Map type"), max_length=25, choices=MAP_TYPES)
    def __unicode__(self):
        return self.language
    def get_absolute_url(self):
        return reverse('slider_view', args=[self.pk])
    class Meta:
        verbose_name = _(u"Google Map")
        verbose_name_plural = _("Google Maps")

class PointMarker(models.Model):
    GMap = models.ForeignKey(GMap)
    title = models.CharField(_(u"Title"), max_length=60)
    image = models.ImageField(_(u"Image"),upload_to="media/slider/images/backgrounds/",null=True,blank=True)
    lat = models.DecimalField(_(u"Latitude"), decimal_places=6, max_digits=9)
    long = models.DecimalField(_(u"Longitude"),decimal_places=6, max_digits=9)
    description = models.TextField(_(u"Description"), max_length=60)
    link = models.URLField(_(u"Link"), max_length=120,null=True, blank=True)
    class Meta:
        verbose_name = _(u"Marker")
        verbose_name_plural = _(u"Markers")


class GMapPlugin(CMSPlugin):
    g_map = models.ForeignKey(GMap)

    def copy_relations(self, oldinstance):
        self.g_map = oldinstance.g_map