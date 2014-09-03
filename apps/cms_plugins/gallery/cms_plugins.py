# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import GalleryPlugin
from django.utils.translation import ugettext as _

class CMSGPlugin(CMSPluginBase):
    model = GalleryPlugin
    name = _("Gallery")
    render_template = "gallery.html"

    def render(self, context, instance, placeholder):

        context.update({
            'gallery': instance.gallery,
            'object': instance,
            'images': instance.gallery.image_set.all(),
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSGPlugin)
