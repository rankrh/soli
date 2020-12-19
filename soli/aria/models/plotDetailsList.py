from aria.models.plot import Plot
from aria.models.plotDetails import PlotDetails
from aria.models.point import Point
from aria.models.shape import Shape


class PlotDetailsList:

    plotDetails = []

    def __init__(self):
        self.plotDetails = []

    def getPlotDetailsByPlotName(self, name):
        self.setPlotDetailsFromPoints(Point.objects.filter(plot__in=Plot.objects.filter(name=name)))

        return self

    def getAllPlotDetails(self):
        plots = Plot.objects.filter(owner=2)
        self.setPlotDetailsFromPlots(plots)

        return self

    def getParentPlots(self):
        plots = Plot.objects.filter(owner=2, parent__isnull=True)
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
                        plot=plot,
                        points=points.filter(shape=plot.shape),
                        children=childDetails
                    )
                )

    def jsonify(self):
        return [plotDetail.jsonify() for plotDetail in self.plotDetails]
