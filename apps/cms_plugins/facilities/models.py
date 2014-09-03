# -*- coding: utf-8 -*-
from adminsortable.models import Sortable
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin



class Attractions(Sortable):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('slider_view', args=[self.pk])

    class Meta(Sortable.Meta):
        verbose_name = _("Attraction")
        verbose_name_plural = _("Attractions")


class Attraction(Sortable):
    attractions = models.ForeignKey(Attractions, verbose_name=_("Attraction set"))
    title = models.CharField(_("Title"), max_length=35)
    image = models.ImageField(_(u"Image"), upload_to="media/gallery/images/")
    image_position = models.CharField(_("Image position"),max_length=5, choices=(
        ('left', _('Left')),
        ('right', _('Right')),
    ))
    description = models.TextField(_("Description"), max_length=1024)
    link = models.BooleanField(_("Add Link?"), default=False)
    url = models.URLField(_("Link"), blank=True, null=True)
    button_text = models.CharField(_("Button text"), max_length=35, blank=True, null=True)

    class Meta(Sortable.Meta):
        verbose_name = _("Attraction")
        verbose_name_plural = _("Attractions")

    def __unicode__(self):
        return self.title


class AttractionsPlugin(CMSPlugin):
    attractions = models.ForeignKey(Attractions)

    def copy_relations(self, oldinstance):
        self.attractions = oldinstance.attractions