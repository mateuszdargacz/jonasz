# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import AttractionsPlugin
from django.utils.translation import ugettext as _

class AttractionsPlugin(CMSPluginBase):
    model = AttractionsPlugin
    name = _("Attractions")
    render_template = "facilities/attractions.html"

    def render(self, context, instance, placeholder):

        context.update({
            'object': instance.attractions,
            'attractions': instance.attractions.attraction_set.all(),
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(AttractionsPlugin)
