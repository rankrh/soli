from aria.models import Point, Plot
from aria.models.plotDetails import PlotDetails


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
            for point in points.distinct('plot'):
                self.plotDetails.append(PlotDetails(plot=point.plot, points=points.filter(plot=point.plot)))

    def jsonify(self):

        return [plotDetail.jsonify() for plotDetail in self.plotDetails]

