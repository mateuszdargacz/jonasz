# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns('cms_plugins.contact_form.views',
                      (r'contact-form/?$', 'ajaxContactForm'),
)
