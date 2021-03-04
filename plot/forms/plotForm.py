from django import forms

from farm.models.plot import Plot


class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ["name", "description", "parent", "type"]

    def savePlot(self, farm, owner):
        plot = self.save(commit=False)
        plot.farm = farm
        plot.owner = owner
        plot.save()

        return plot
