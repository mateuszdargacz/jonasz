from django.contrib import admin
from django.core.mail import send_mail

from reservation.models import Contact, CalendarDay, PriceSettings
from datetime import date, timedelta as td

class ContactAdmin(admin.ModelAdmin):
    list_display = ['apartament','last_name', 'start_date', 'end_date',
                    'client_email_address', 'phone', 'created_date','confirmation_data','confirmation_payment']
    def data_confirmation(self, request, queryset):
        rows_updated = queryset.update(confirmation_data=True)
        for obj in queryset:
            send_mail(u'Confirmation of Data Veriyfication',u'Thanks, your data is beeing processed','APARTAMENTY.PL <RECEPCJA@APARTAMENTY.PL>', [obj.client_email_address])
        if rows_updated == 1:
            message_bit = "1 reservation data was confirmed"
        else:
            message_bit = "%s reservation data were confirmed" % rows_updated
        self.message_user(request, "%s successfully completed." % message_bit)



    def payment_confirmation(self, request, queryset):
        rows_updated = queryset.update(confirmation_payment=True)
        for obj in queryset:
            d1 = obj.start_date
            d2 = obj.end_date
            delta = d2 - d1
            for i in range(delta.days + 1):
                day = CalendarDay()
                date =  d1 + td(days=i)
                day.apartament = obj.apartament
                day.date = date
                day.price = 0
                day.state = 2
                day.save()
            send_mail(u'Confirmation of Payment Veriyfication',u'We are waiting for your arrival','APARTAMENTY.PL <RECEPCJA@APARTAMENTY.PL>', [obj.client_email_address])
        if rows_updated == 1:
            message_bit = "1 reservation payment was confirmed"
        else:
            message_bit = "%s reservation payment were confirmed" % rows_updated
        self.message_user(request, "%s successfully completed." % message_bit)

    actions = ['data_confirmation','payment_confirmation']
    data_confirmation.short_description = "Mark selected reservations as data confirmed"
    payment_confirmation.short_description = "Mark selected reservations as payment confirmed"

class CalendarDayAdmin(admin.ModelAdmin):
    list_display = ('apartament', 'date', 'price', 'state')
    list_filter = ('state',)
    date_hierarchy = 'date'

class PriceSettingsAdmin(admin.ModelAdmin):
    list_display = ('price', 'show_default_price')
    
    # def has_add_permission(self, request):
    #     if PriceSettings.objects.exists():
    #         return False
    #     return True


admin.site.register(CalendarDay, CalendarDayAdmin)
admin.site.register(PriceSettings, PriceSettingsAdmin)
admin.site.register(Contact, ContactAdmin)