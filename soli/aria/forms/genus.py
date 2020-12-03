from aria.forms.templates.templates import createTextInput
from aria.models import Genus
from django import forms


class CreateGenusForm(forms.ModelForm):
    class Meta:
        model = Genus
        fields = ["ge_name"]
        widgets = {"ge_name": createTextInput("Genus Name")}

    def saveGenus(self, request):
        genus = self.save(commit=False)
        genus.save()
        return genus

    def isUnique(self):
        genus = self.cleaned_data['ge_name']
        return not Genus.objects.filter(genus=genus).exists()
