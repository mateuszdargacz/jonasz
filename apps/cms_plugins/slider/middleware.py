from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class SliderMediaMiddleware(object):
    def process_request(self, request):
        if '/media/' in request.path and ('pl' in request.path or 'en' in request.path) and not hasattr(request, 'redirected'):
            path = request.path.split('/media/')[-1]
            request.redirected = True
            request.path = settings.MEDIA_URL + path
            return HttpResponsePermanentRedirect(request.path)
