from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('reservation.views',
    url(r'^$', 'contact', name='contact-form'),
    url(r'^calendar/month/(?P<year>\d+)/(?P<month>\d{1,2})/(?P<slug>[-\w]+)/$',
        'month_calendar', name='month_calendar'),
    url(r'^confirm_reservation/secret_link/(?P<pk>\d+)/$',
        'confirm_reservation', name='confirm_reservation'),
    url(r'^cancel_reservation/secret_link/(?P<pk>\d+)/$',
        'cancel_reservation', name='cancel_reservation'),

)

