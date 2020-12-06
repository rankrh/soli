from django import forms

from aria.models import Plot


initialValues = {"plt_name": "Unnamed Plot", "plt_description": ""}

class PlotForm(forms.ModelForm):

    class Meta:
        model = Plot
        fields = ["plt_name", "plt_description", "plt_area", "plt_parent_num", "plt_cr_num"]

    def savePlot(self):
        plot = self.save(commit=False)
        plot.save()