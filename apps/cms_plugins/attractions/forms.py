from django import forms

from gmapi.forms.widgets import GoogleMap


class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width': '100%', 'height': 500, 'scrollwheel': 'false'}))

