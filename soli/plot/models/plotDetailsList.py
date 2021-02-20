from farm.models.farm import Farm
from geometry.models.point import Point
from geometry.models.shape import Shape
from plot.models.plot import Plot
from plot.models.plotDetails import PlotDetails


class PlotDetailsList:
    plotDetails = []

    def __init__(self, owner):
        self.plotDetails = []
        self.owner = owner
        self.farm = Farm.objects.filter(owner=self.owner).get()

    def getPlotDetailsByPlotName(self, name):

        if self.owner is not None:
            self.setPlotDetailsFromPoints(
                Point.objects.filter(plot__in=Plot.objects.filter(owner=self.owner, name=name))
            )

        return self

    def getPlotDetailsForUser(self):
        if self.owner is not None:
            plots = Plot.objects.filter(owner=self.owner)
            self.setPlotDetailsFromPlots(plots)

        return self

    def getParentPlots(self):
        if self.owner is not None:
            plots = Plot.objects.filter(owner=self.owner, parent__isnull=True)
            self.setPlotDetailsFromPlots(plots)

        return self

    def setPlotDetailsFromPlots(self, plots):
        points = Point.objects.filter(shape__in=Shape.objects.filter(plot__in=plots))

        for plot in plots:
            if plot.parent is None:
                children = plots.filter(parent=plot)
                childDetails = [PlotDetails(plot=child, points=points.filter(shape=child.shape)) for child in children]

                self.plotDetails.append(
                    PlotDetails(
                        owner=self.owner,
                        farm=self.farm,
                        plot=plot,
                        points=points.filter(shape=plot.shape),
                        children=childDetails
                    )
                )

    def jsonify(self):
        return [plotDetail.jsonify() for plotDetail in self.plotDetails]
