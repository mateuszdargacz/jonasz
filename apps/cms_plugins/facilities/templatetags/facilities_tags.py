import random
from django import template
register = template.Library()

@register.assignment_tag
def shuffle():
    return random.choice(["red", "green", "yellow", "sea"])
