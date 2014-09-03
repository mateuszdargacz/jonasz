# -*- coding: utf-8 -*-
from apps.cms_plugins.attractions.forms import MapForm
from apps.cms_plugins.attractions.models import TO_MAPS_OBJ
from django import template

from gmapi import maps
from gmapi.forms.widgets import GoogleMap

register = template.Library()


@register.assignment_tag
def render_map(Gmap, markers=None):
    if Gmap and markers:
        gmap = maps.Map(opts={
            'center': maps.LatLng(Gmap.center_lat, Gmap.center_long),
            'mapTypeId': TO_MAPS_OBJ[Gmap.map_type],
            'zoom': Gmap.zoom,
            'scrollwheel': False,
            'mapTypeControlOptions': {
                'style': maps.MapTypeControlStyle.DROPDOWN_MENU
            },
        })
        for marker in markers:
            _marker = maps.Marker(opts={
                'map': gmap,
                'position': maps.LatLng(marker.lat, marker.long),
            })
            maps.event.addListener(_marker, 'mouseover', 'myobj.markerOver')
            maps.event.addListener(_marker, 'mouseout', 'myobj.markerOut')
            if marker.link:
                info_content = """
                                <a href="%s"><h2>%s</h2></a>
                                <p>%s</p>
                               """ % (marker.link, marker.title, marker.description)
            else:
                info_content = """
                                <h2>%s</h2>
                                <p>%s</p>
                               """ % (marker.title, marker.description)

            info = maps.InfoWindow({
                'content': info_content,
                'disableAutoPan': True
            })
            info.open(gmap, _marker)

        return MapForm(initial={'map': gmap})

    return None