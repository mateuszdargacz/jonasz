# -*- coding: utf-8 -*-
from django import forms

from reservation.models import Contact
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.ModelForm):
    # expiry_date = ExpiryDateField(label=_('Card expiry date *'))
    # card_number = CreditCardField(label=_('Card number *'))
    # name_on_card = forms.CharField(label=_("Card holder name *"))
    # card_code = VerificationValueField(label=_("CVV or CVC *"))
    def __init__(self,request=None, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['client_email_address'].error_messages['invalid'] = _('Please enter a valid email address.')
        self.fields['personal_data'].required = True
        if request.GET:
            self.fields['start_date'].initial = request.GET.get('start')
            self.fields['end_date'].initial = request.GET.get('end')
            self.fields['apartament'].initial = request.GET.get('name')
    class Meta:
        model = Contact

        exclude = ['created_date', 'confirmation_data', 'confirmation_payment']
        widgets = {
            #'address': forms.Textarea(attrs={'rows':3}),
            #'main_app_access': forms.CheckboxInput({'checked': 'checked', 'disabled':'disabled'}),
            'additional_notes': forms.Textarea(attrs={'rows':3}),
        }
    def clean(self):

        return self.cleaned_data

    
#    def clean(self):
#        c = self.cleaned_data
#        if not self.errors and not c['client_email_address'] and not c['phone']:
#            raise forms.ValidationError('Podaj email lub telefon.')
#
#        return c