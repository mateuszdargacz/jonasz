from adminsortable.admin import SortableStackedInline, SortableAdmin
from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Attractions, Attraction


class AttractionInline(SortableStackedInline):
    model = Attraction
    extra = 1


class AttractionsAdmin(SortableAdmin):
    inlines = [AttractionInline, ]

admin.site.register(Attractions, AttractionsAdmin)