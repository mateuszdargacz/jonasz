# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns('reservation.views',
    (r'^$', 'index'),
)