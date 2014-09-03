from django.conf.urls import *

urlpatterns = patterns('apartaments.views',
    url(r'^$', 'apartaments_list', name='apartaments_list'),
    url(r'^search$', 'apartaments_free_list', name='apartaments_free_list'),
    url(r'^(?P<slug>[-\w]+)$', 'apartament_detail', name='apartament_detail'),
)

