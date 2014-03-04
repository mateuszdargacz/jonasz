# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey
from reservation.html_calendar import PriceHTMLCalendar
from apartaments.models import Apartament
from django.core.mail import send_mail

def formatted_price(price):
    price = str(price)
    if price.endswith('.00'):
        return price[:-3]
    return price


class Contact(Sortable):
    apartament = SortableForeignKey(Apartament, related_name='Apartament',
                               verbose_name=_('Apartament'))
    last_name = models.CharField(_('Contact person'), max_length=200, blank=True)
    start_date = models.DateTimeField(_('Booking from *'),)
    end_date = models.DateTimeField(_('Booking to *'), )
    client_email_address = models.EmailField(_('E-mail'), max_length=60,
                                             blank=True, null=True)
    phone = models.DecimalField(_('Phone'), max_digits=12, decimal_places=0 )
    created_date = models.DateTimeField(auto_now_add=True)
    personal_data = models.BooleanField(_('I agree to the processing of personal data'))
    confirmation_data = models.BooleanField(_('Confirmation of data'))
    confirmation_payment = models.BooleanField(_('Confirmation of payment'))

    class Meta:
        verbose_name = u'Rezerwacja'
        verbose_name_plural = u'Rezerwacje'

    def save(self, *args, **kwargs):
        if self.id:
            old_reservation = Contact.objects.get(pk=self.id)
            if(old_reservation.confirmation_data == False and self.confirmation_data == True):
                send_mail(u'Confirmation of Data Veriyfication',u'Thanks, your data is beeing processed', settings.DEFAULT_FROM_EMAIL, [self.client_email_address, ]+settings.CONTACT_EMAIL_TO)
            if(old_reservation.confirmation_payment == False and self.confirmation_payment == True):
                send_mail(u'Confirmation of Payment Veriyfication',u'We are waiting for your arrival', settings.DEFAULT_FROM_EMAIL, [self.client_email_address, ] + settings.CONTACT_EMAIL_TO)
        super(Contact, self).save(*args, **kwargs)


class CalendarDayManager(models.Manager):
    def get_by_date(self, year, month, slug):
        return self.all().filter(date__year=year, date__month=month, apartament__slug=slug)

    def get_html_calendar(self, year, month, slug):
        prices = self.get_by_date(year=year, month=month, slug=slug)
        try:
            settings = PriceSettings.objects.get(apartament__slug=slug)
        except:
            settings = None
        return PriceHTMLCalendar(prices, settings, slug).formatmonth(year, month)


class CalendarDay(Sortable):
    apartament = SortableForeignKey(Apartament, related_name='calendar',
                               verbose_name=_('calendar'))
    date = models.DateField(u'Data')
    price = models.DecimalField(u'Cena', max_digits=10, decimal_places=2)
    STATE_FREE = 1
    STATE_BOOKING = 2
    STATE_UNAVAILABLE = 3
    STATE_CHOICES = (
        (STATE_FREE, _('Free')),
        (STATE_BOOKING, _('Booking')),
        (STATE_UNAVAILABLE, _('Unavailable')),
    )
    state = models.PositiveSmallIntegerField(u'Stan', choices=STATE_CHOICES,
                                             default=STATE_FREE)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = CalendarDayManager()

    class Meta:
        ordering = ('-date',)
        verbose_name = u'Dzień kalendarza'
        verbose_name_plural = u'Dni kalendarza'
        unique_together = ('apartament', 'date')

    def __unicode__(self):
        return str(self.date)

    @property
    def formatted_price(self):
        return formatted_price(self.price)


class PriceSettings(Sortable):
    apartament = SortableForeignKey(Apartament, related_name='price',
                               verbose_name=_('price'), unique=True)
    price = models.DecimalField(u'Cena', max_digits=10, decimal_places=2)
    show_default_price = models.BooleanField(u'Pokazuj domyślną cenę',
                                             default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Cena domyślna'
        verbose_name_plural = u'Cena domyślna'

    @property
    def state(self):
        return CalendarDay.STATE_FREE

    def get_state_display(self):
        return unicode(dict(CalendarDay.STATE_CHOICES)[self.state])

    @property
    def formatted_price(self):
        return formatted_price(self.price)