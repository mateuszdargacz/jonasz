# -*- coding: utf-8 -*-
import datetime

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from reservation.models import CalendarDay
from reservation.forms import ContactForm


class ContactFormPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("reservation form")
    render_template = "reservation/contact_plugin.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        
        form = ContactForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            # Process the data in form.cleaned_data
            send_mail(u'Rezerwacja ze strony http://gdynia-magnolia.pl',
                      u'Osoba kontaktowa: %s,\nRezerwacja od: %s,\nRezerwacja do: %s,\nAdres e-mail: %s,\nTel.: %s,\nWłaściciel karty: %s, \nData ważności: %s, \nNr kart: %s, \nNr weryfikacyjny: %s' % (obj.last_name, obj.start_date, obj.end_date, obj.client_email_address, obj.phone, obj.name_on_card, obj.expiry_date, obj.card_number, obj.card_code ), settings.DEFAULT_FROM_EMAIL, settings.CONTACT_EMAIL_TO)
            if obj.client_email_address:
                send_mail(u'Wiadomość ze strony gdynia-magnolia.pl potwierdzenie rezerwacji', u'Dziękujemy za rezerwację. Odpowiemy tak szybko jak to możliwe.', settings.DEFAULT_FROM_EMAIL, [obj.client_email_address])
            return HttpResponseRedirect('/thanks/') # Redirect after POST
        
        context['form'] = form
        return context

plugin_pool.register_plugin(ContactFormPlugin)


class PriceCalendarPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("price calendar")
    render_template = "reservation/price_calendar.html"

    def render(self, context, instance, placeholder):
        now = datetime.datetime.now()

        context['calendar'] = CalendarDay.objects.get_html_calendar(now.year,
                                                                    now.month)
        return context

plugin_pool.register_plugin(PriceCalendarPlugin)