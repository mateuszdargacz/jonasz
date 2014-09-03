from cms_plugins.gallery.models import CATEGORY_CHOICES
from django.templatetags.i18n import register


@register.assignment_tag
def get_categories():
    return CATEGORY_CHOICES