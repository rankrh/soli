from aria.forms.templates.templates import createTextInput
from django import forms

from aria.models.genus import Genus


class CreateGenusForm(forms.ModelForm):
    class Meta:
        model = Genus
        fields = ["name"]
        widgets = {"name": createTextInput("Genus Name")}

    def saveGenus(self, request):
        genus = self.save(commit=False)
        genus.save()
        return genus

    def isUnique(self):
        genus = self.cleaned_data['name']
        return not Genus.objects.filter(genus=genus).exists()
