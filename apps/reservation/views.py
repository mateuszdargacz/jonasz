# -*- coding: utf-8 -*-
from datetime import date, timedelta as td
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from apartaments.models import Apartament
from reservation.forms import ContactForm
from reservation.models import CalendarDay, Contact
import datetime


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request, request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            obj = form.save()
            # Process the data in form.cleaned_data
            confirm = 'agroturystykaumarleny.pl/pl/reservation/confirm_reservation/secret_link/%s/' % obj.pk
            cancel = 'agroturystykaumarleny.pl/pl/reservation/cancel_reservation/secret_link/%s/' % obj.pk

            send_mail(u'Rezerwacja ze strony Agroturystykaumarleny.pl',
                      u'Osoba kontaktowa: %s,\nRezerwacja od: %s,\nRezerwacja do: %s,\nAdres e-mail: %s,\nTel.: %s\nPotwierdzenie rezerwacji:\n%s\nAnulowanie rezerwacji:\n%s' % (
                          obj.last_name, obj.start_date, obj.end_date, obj.client_email_address, obj.phone, confirm, cancel),
                      settings.DEFAULT_FROM_EMAIL, settings.CONTACT_EMAIL_TO)
            if obj.client_email_address:
                send_mail(_("Reservation from Agroturystykaumarleny.pl"),
                          _("Thanks for booking, We will contact you as soon as possible") + settings.EMAIL_FOOTER,
                          settings.DEFAULT_FROM_EMAIL, [obj.client_email_address])

            return HttpResponseRedirect('/' + request.LANGUAGE_CODE + '/thanks/') # Redirect after POST
        else:
            return render(request, 'reservation/contact.html', {'form': form})
    elif request.method == 'GET':
        # form = ContactForm(self.fields['start_date']=request.GET)
        form = ContactForm(request=request)
        context = {'form': form, }

        if request.GET.get('name'):
            context.update({
                'pk': request.GET.get('name'),
            })

        if request.GET.get('start') and request.GET.get('end'):
            d1 = datetime.datetime.strptime(request.GET.get('start'), '%Y-%m-%d').date()
            d2 = datetime.datetime.strptime(request.GET.get('end'), '%Y-%m-%d').date()
            duration = d2 - d1
            apartament = Apartament.objects.all().filter(pk=request.GET.get('name'))[0]
            context.update({
                'start': d1,
                'end': d2,
                'duration': duration.days,
                'apartament': apartament,
            })
        return render(request, 'reservation/contact.html', context)


def month_calendar(request, year, month, slug):
    try:
        month = datetime.date(year=int(year), month=int(month), day=1)
    except ValueError:
        raise Http404
    get_object_or_404(Apartament, slug=slug)
    return HttpResponse(
        CalendarDay.objects.get_html_calendar(month.year, month.month, slug))


def confirm_reservation(request, pk):
    context = {}
    contact = Contact.objects.get(pk=pk)
    contact.confirmation_data, contact.confirmation_payment = True, True
    subject = _(u'Confirmation of Payment Veriyfication')
    content = _("Thanks, We recieved your payment.\n We are waiting for your arrival!") + settings.EMAIL_FOOTER
    d1 = contact.start_date
    d2 = contact.end_date
    delta = d2 - d1
    try:
        for i in range(delta.days + 1):
            day = CalendarDay()
            date = d1 + td(days=i)
            day.apartament = contact.apartament
            day.date = date
            day.price = 0
            day.state = 2
            day.save()
        send_mail(subject, content, settings.DEFAULT_FROM_EMAIL, [contact.client_email_address])
        contact.save()
        context['contact'] = contact
    except:
        pass
    return render(request, 'reservation/confirm_reservation.html', context)
def cancel_reservation(request, pk):
    context = {}
    contact = Contact.objects.get(pk=pk)
    contact.confirmation_data, contact.confirmation_payment = True, True
    subject = _(u'Reservation canceled')
    content = _("Reservation has been canceled.\n") + settings.EMAIL_FOOTER
    d1 = contact.start_date
    d2 = contact.end_date
    delta = d2 - d1
    try:
        for i in range(delta.days + 1):
            day = CalendarDay.objects.get(date=d1 + td(days=i))
            day.delete()
        context['contact'] = contact
        send_mail(subject, content, settings.DEFAULT_FROM_EMAIL, [contact.client_email_address])

    except:
        pass
    return render(request, 'reservation/cancel_reservation.html', context)
