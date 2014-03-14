from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^ajax/',include('cms_plugins.contact_form.urls', namespace='ajax')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/', include(admin.site.urls)),


)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'^thanks/$', TemplateView.as_view(template_name='cms/sites/thanks.html')),
    url(r'^reservation/',include('reservation.urls',namespace='reservation')),
    url(r'^apartaments/',include('apartaments.urls',namespace='apartaments')),
    url(r'^', include('cms.urls')),
)