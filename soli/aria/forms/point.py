from django.forms import forms

from aria.models import Point


class PointForm(forms.ModelForm):

    class Meta:
        model = Point
        fields = ["pt_plt_num", "pt_order", "pt_lat", "pt_long"]
