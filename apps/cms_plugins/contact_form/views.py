# -*- coding: utf-8 -*-
import json

from django.core.mail import EmailMessage

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def ajaxContactForm(request):
    context= {}
    if request.is_ajax():
        subject = u"[AgroturystykaUMarleny.pl] Pytanie z formularza"
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        try:
            message_to_user = render_to_string('mail/contact_form.html',
                                                          {   'name'   : name,
                                                              'email'  : email,
                                                              'phone'  : phone,
                                                              'message': message})
            print "pre-sent"
            mail = EmailMessage(subject,
                            message_to_user,
                            settings.DEFAULT_FROM_EMAIL,
                            settings.CONTACT_EMAIL_TO,
                            )

            mail.content_subtype = "html"
            mail.send()
            print "sent"
            context ={
                'done': True,
                'message': u'Twoja wiadomość została wysłana',
            }
        except Exception as e:
            print ('%s (%s)' % (e.message, type(e)))
            context ={
                'done': False,
                'message': u'Wysyłanie wiadomości się nie powiodło, prosimy o inną formę kontaktu',
            }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        raise Http404