from aria.forms.templates.templates import createNumberInput, createRadioInput
from aria.models import Crop, Harvest
from aria.models.validation.harvest import CROP_TYPE
from django.forms import inlineformset_factory

harvestFormset = inlineformset_factory(
    Crop,
    Harvest,
    fields=[
        "har_begin",
        "har_end",
        "har_variety"
    ],
    extra=1,
    can_delete=False,
    widgets={
        "har_begin": createNumberInput("Start Date", 1),
        "har_end": createNumberInput("End Date", 1),
        "har_variety": createRadioInput(choices=CROP_TYPE)
    }
)


class HarvestFormSet(harvestFormset):

    def __init__(self, *args, **kwargs):
        super(HarvestFormSet, self).__init__(*args, **kwargs)

        for form in self.forms:
            form.empty_permitted = False
