from farm.models.farm import Farm
from geometry.models.point import Point
from geometry.models.shape import Shape
from farm.models.plot import Plot
from farm.models.plotDetails import PlotDetails


class PlotDetailsList:
    plotDetails = []

    def __init__(self, farmer, farm=None):
        self.plotDetails = []
        self.farmer = farmer
        self.farm = (
            farm if farm is not None else Farm.objects.filter(farmer=self.farmer)
        )

    def getPlotDetailsByPlotName(self, name):

        if self.farmer is not None:
            self.setPlotDetailsFromPoints(
                Point.objects.filter(
                    plot__in=Plot.objects.filter(farmer=self.farmer, name=name)
                )
            )

        return self

    def getPlotDetailsForUser(self):
        if self.farmer is not None:
            plots = Plot.objects.filter(farmer=self.farmer)
            self.setPlotDetailsFromPlots(plots)

        return self

    def getParentPlots(self):
        if self.famer is not None:
            plots = Plot.objects.filter(farmer=self.farmer, parent__isnull=True)
            self.setPlotDetailsFromPlots(plots)

        return self

    def setPlotDetailsFromPlots(self, plots):
        points = Point.objects.filter(shape__in=Shape.objects.filter(plot__in=plots))

        for plot in plots:
            if plot.parent is None:
                children = plots.filter(parent=plot)
                childDetails = [
                    PlotDetails(plot=child, points=points.filter(shape=child.shape))
                    for child in children
                ]

                self.plotDetails.append(
                    PlotDetails(
                        farmer=self.farmer,
                        farm=self.farm,
                        plot=plot,
                        points=points.filter(shape=plot.shape),
                        children=childDetails,
                    )
                )

    def jsonify(self):
        return [plotDetail.jsonify() for plotDetail in self.plotDetails]
