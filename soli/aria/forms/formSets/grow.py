from aria.forms.templates.templates import createRadioInput, createTextInput
from aria.models.crop import Crop
from aria.models.growplan import GrowPlan
from aria.models.validation.growValidation import SUN
from django.forms import inlineformset_factory, forms

growFormSet = inlineformset_factory(
        Crop,
        GrowPlan,
        fields=[
            "sun",
            "soil"
        ],
        extra=1,
        can_delete=False,
        widgets={
            "sun": createRadioInput(choices=SUN),
            "soil": createTextInput(placeholder="Soil type")
        })


class GrowFormSet(growFormSet):

    def __init__(self, *args, **kwargs):
        super(GrowFormSet, self).__init__(*args, **kwargs)

        for form in self.forms:
            form.empty_permitted = False
