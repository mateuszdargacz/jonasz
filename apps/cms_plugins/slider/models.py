# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin

PLACEMENT_CHOICES =[
    ('l',u'lewo'),
    ('c',u'środek'),
    ('r',u'prawo'),

]



class Slider(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('slider_view', args=[self.pk])
    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Sliders")

class Slide(models.Model):
    slider = models.ForeignKey(_("Slider"))
    background = models.ImageField(_(u"Slider background"), upload_to="media/slider/images/backgrounds/")

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")

class SlideObj(models.Model):
    obj_type = models.CharField(_("Object type"), max_length=25, choices={
                                                                ("1", _("Image")),
                                                                ("2", _("Button")),
                                                                ("3", _("Text")),
                                                                ("4", _("List text")),
                                                                })

    slide = models.ForeignKey(Slide, verbose_name=_("Slide"))
    image = models.ImageField(_("image"), upload_to="media/sliderobj/images/", null=True, blank=True)
    description = models.CharField(_("Text"), max_length=60, blank=True, null=True)
    link = models.URLField(_("Link"), max_length=120, null=True, blank=True)
    link_name = models.CharField(_("Link name"), max_length=60, null=True, blank=True)
    image_position_vertical = models.DecimalField(_("Vertical location"), max_digits=3, decimal_places=0,
                                                  help_text=_("space from top"), blank=True, null=True)
    image_position_horizontal = models.DecimalField(_("horizontal location"), max_digits=3, decimal_places=0,
                                                    help_text=_("space from left"), blank=True, null=True)


    class Meta:
        verbose_name = _("Slide object")
        verbose_name_plural = _("Slide objects")

class SliderPlugin(CMSPlugin):
    slider = models.ForeignKey(Slider)

    def copy_relations(self, oldinstance):
        self.slider = oldinstance.slider