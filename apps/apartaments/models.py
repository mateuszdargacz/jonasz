from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey
from tinymce.models import HTMLField
import reservation.models


class Apartament(Sortable):

    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    rooms = models.IntegerField()
    maxPeople = models.IntegerField()
    surface = models.IntegerField()

    teaserText = HTMLField(_('teaserText'))
    description = HTMLField(_('Description'))

    teaserPicture = models.ImageField(_('Teaser Picture'), upload_to='apartaments')

    published = models.BooleanField(_('Published'), default=True)

    class Meta(Sortable.Meta):
        verbose_name = _('Apartament')
        verbose_name_plural = _('Apartaments')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super(Apartament, self).save(*args, **kwargs)

class Photos(Sortable):
    apartament = SortableForeignKey(Apartament, related_name='slides',
                               verbose_name=_('Gallery'))

    published = models.BooleanField(_('Published'), default=True)

    imageField1 = models.ImageField(_('Image'), upload_to='apartaments',
                                    blank=True)
    imageField2 = models.ImageField(_('Image'), upload_to='apartaments',
                                    blank=True)
    imageField3 = models.ImageField(_('Image'), upload_to='apartaments',
                                    blank=True)

    template = models.CharField(max_length=255, choices=(('1', 'one photo'),
                                                         ('2', 'two photo'),
                                                         ('3', 'three photo')
    ))

    class Meta(Sortable.Meta):
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    def __unicode__(self):
        return self.apartament.name
