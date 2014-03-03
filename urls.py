from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^ajax/',include('cms_plugins.contact_form.urls', namespace='ajax')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/', include(admin.site.urls)),


)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'^reservation/',include('reservation.urls',namespace='reservation')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)