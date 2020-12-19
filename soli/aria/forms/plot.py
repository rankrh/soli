from django import forms

from aria.models.plot import Plot


class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ["name", "description", "parent", "type"]

    def savePlot(self, plotType=None):
        plot = self.save(commit=False)
        plot.save()

        return plot
