from django import forms
from ..models import Crop


class CreateCropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = [
            "variety", "taxonomy", "height", "weight", "yieldKg", "gallonsPerWeek", "sunPerDay", "category",
            "daysToHarvest"
        ]
        widgets = {
            "variety": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Crop variety'
            })
        }
