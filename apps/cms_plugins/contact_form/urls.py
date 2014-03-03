# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('cms_plugins.contact_form.views',
                      (r'contact-form/?$', 'ajaxContactForm'),
)
