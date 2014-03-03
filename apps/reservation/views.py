# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse


from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap


class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))


def index(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(38, -97),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    marker = maps.Marker(opts = {
        'map': gmap,
        'position': maps.LatLng(38, -97),
    })
    maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
    maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
    info = maps.InfoWindow({
        'content': 'Hello!',
        'disableAutoPan': True
    })
    info.open(gmap, marker)

    marker1 = maps.Marker(opts = {
        'map': gmap,
        'position': maps.LatLng(38, -96),
    })
    maps.event.addListener(marker1, 'mouseover', 'myobj.markerOver')
    maps.event.addListener(marker1, 'mouseout', 'myobj.markerOut')
    info = maps.InfoWindow({
        'content': '<h2>Hi</h2>',
        'disableAutoPan': True
    })
    info.open(gmap, marker1)
    context = {'form': MapForm(initial={'map': gmap})}
    return render_to_response('reservation/sites/home.html', context)