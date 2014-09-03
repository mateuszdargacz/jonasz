from django.contrib import admin

from .models import Slide, Slider, SlideObj


class SlideObjInline(admin.TabularInline):
    model = SlideObj
    extra = 1


class SlideInline(admin.TabularInline):
    model = Slide
    extra = 1


class SlideAdmin(admin.ModelAdmin):
    model = Slide
    inlines = [SlideObjInline, ]


class SliderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Slide, SlideAdmin)
admin.site.register(Slider, SliderAdmin)