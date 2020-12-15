from aria.models.plot import Plot
from aria.models.plotDetails import PlotDetails
from aria.models.point import Point


class PlotDetailsList:

    plotDetails = []

    def __init__(self):
        self.plotDetails = []

    def getPlotDetailsByPlotName(self, name):
        self.setPlotDetailsFromPoints(Point.objects.filter(plot__in=Plot.objects.filter(name=name)))

        return self

    def getAllPlotDetails(self):
        self.setPlotDetailsFromPoints(Point.objects.all())

        return self

    def setPlotDetailsFromPoints(self, points):

        if points is not None and points.exists():
            for point in points.distinct('shape'):
                plot = Plot.objects.filter(shape=point.shape).get()
                self.plotDetails.append(PlotDetails(plot=plot, points=points.filter(shape=point.shape)))

    def jsonify(self):

        return [plotDetail.jsonify() for plotDetail in self.plotDetails]

