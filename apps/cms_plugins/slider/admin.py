from .forms import SlideObjForm
from django.contrib import admin

from .models import Slide, Slider, SlideObj
from nested_inlines.admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin


class SlideObjInline(NestedStackedInline):
    model = SlideObj
    extra = 1
    class Media:
        js = ("js/admin_slider.js",)

class SlideInline(NestedStackedInline):
    model = Slide
    extra = 1
    inlines = [SlideObjInline, ]


class SliderAdmin(NestedModelAdmin):
    inlines = [SlideInline, ]

admin.site.register(Slider, SliderAdmin)