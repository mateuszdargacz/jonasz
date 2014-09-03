# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import GMapPlugin
from django.utils.translation import ugettext as _

class CMSGMapPlugin(CMSPluginBase):
    model = GMapPlugin
    name = _("GoogleMap")
    render_template = "attractions.html"

    def render(self, context, instance, placeholder):
        context.update({
            'g_map': instance.g_map,
            'object': instance,
            'markers': instance.g_map.pointmarker_set.all(),
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSGMapPlugin)
