from copy import copy
import random
from django.templatetags.i18n import register


@register.filter
def subtract(value, arg):
    return int(value) - arg

@register.assignment_tag
def randomize_slides(queryset):
    max_num = queryset.count()
    nums = []
    pks = list(queryset.values("pk"))
    for i in xrange(4):
        a = random.choice(pks)
        pks.remove(a)
        nums.append(a['pk'])
    queryset = queryset.filter(pk__in=nums)
    return queryset

@register.simple_tag
def shitty_parse_hack(string, phrase1, pharse2):
    phrases=[phrase1,pharse2]
    print phrases
    for phrase in phrases:
        st = string.split(phrase)
        st[0] += "<br>"+phrase
        string = ''.join(st)
    return string