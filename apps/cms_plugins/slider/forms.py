from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from .models import SlideObj


class SlideObjForm(forms.ModelForm):
    class Meta:
        model = SlideObj
        fields = ['obj_type', 'description', 'image', 'link', 'link_name', 'image_position_vertical', 'image_position_horizontal']

    obj_type = forms.ChoiceField(label=_("Object type"), choices= {
        "1": _("Image"),
        "2": _("Button"),
        "3": _("Text"),
        "4": _("List text"),


    })

    def clean(self):
        cleaned_data = super(SlideObjForm,self).clean()
        obj_type = cleaned_data['obj_type']
        if obj_type == "1" and not cleaned_data.get('image'):
            raise ValidationError(_("This field is required."))
        elif obj_type == "2" and not cleaned_data.get('button'):
            raise ValidationError(_("This field is required."))
        elif obj_type in ("3", "4") and not cleaned_data.get('text'):
            raise ValidationError(_("This field is required."))
        return cleaned_data