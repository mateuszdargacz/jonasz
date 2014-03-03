from django.templatetags.i18n import register


@register.filter
def subtract(value, arg):
    return int(value) - arg