# -*- coding: utf-8 -*-
from django.contrib import admin

from models import GMap, PointMarker

class PointMarkerInline(admin.StackedInline):
    model = PointMarker

class GMapAdmin(admin.ModelAdmin):
    inlines = [PointMarkerInline]

admin.site.register(GMap, GMapAdmin)