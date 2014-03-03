from adminsortable.admin import SortableStackedInline, SortableAdmin
from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Gallery, Image


class ImageInline(SortableStackedInline):
    model = Image
    extra = 1


class GalleryAdmin(SortableAdmin):
    inlines = [ImageInline, ]

admin.site.register(Gallery, GalleryAdmin)