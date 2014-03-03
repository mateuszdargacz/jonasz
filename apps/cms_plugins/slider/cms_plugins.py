# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import SliderPlugin
from django.utils.translation import ugettext as _

class CMSGalleryPlugin(CMSPluginBase):
    model = SliderPlugin
    name = _("Slider")
    render_template = "slider.html"

    def render(self, context, instance, placeholder):

        context.update({
            'slider':instance.slider,
            'object':instance,
            'slides': instance.slider.slide_set.all(),
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)
