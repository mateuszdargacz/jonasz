from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline
from .models import Apartament, Photos


class Photo(SortableTabularInline):
    fields = ('template', 'imageField1', 'imageField2', 'imageField3')
    model = Photos
    extra = 1

class StoryAdmin(SortableAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = (Photo,)

admin.site.register(Apartament, StoryAdmin)
