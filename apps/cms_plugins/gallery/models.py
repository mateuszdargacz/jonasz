# -*- coding: utf-8 -*-
from adminsortable.models import Sortable
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin

CATEGORY_CHOICES = [
    ('1', _("Apartments")),
    ('2', _("Atractions")),
    ('3', _("Landscape")),
]



class Gallery(Sortable):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('slider_view', args=[self.pk])

    class Meta(Sortable.Meta):
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")

class Image(Sortable):
    gallery = models.ForeignKey(Gallery, verbose_name=_("Gallery"))
    title = models.CharField(_("Title"), max_length=35)
    image = models.ImageField(_(u"Image"), upload_to="media/gallery/images/")
    size = models.CharField(_("Category"), max_length=1, choices=CATEGORY_CHOICES)

    class Meta(Sortable.Meta):
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __unicode__(self):
        return self.title




class GalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(Gallery)

    def copy_relations(self, oldinstance):
        self.gallery = oldinstance.gallery