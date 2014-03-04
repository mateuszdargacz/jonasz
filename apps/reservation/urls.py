from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('reservation.views',
    url(r'^$', 'contact', name='contact-form'),
    url(r'^calendar/month/(?P<year>\d+)/(?P<month>\d{1,2})/(?P<slug>[-\w]+)/$',
        'month_calendar', name='month_calendar'),
)

