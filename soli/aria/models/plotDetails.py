import json

from django.shortcuts import get_object_or_404

from aria.forms.plot import PlotForm
from aria.models import Plot, Point


class PlotDetails:
    plot = None
    plotForm = None
    coordinates = []
    points = []

    def __init__(self, request=None, plot=None, points=None):

        self.resetDetails()
        if request is not None:
            plotId = request.POST.get("id")
            if plotId is not None:
                self.plot = get_object_or_404(Plot, id=plotId)

            self.plotForm = PlotForm(request.POST, instance=self.plot)
            self.coordinates = json.loads(request.POST["points"]) if "points" in request.POST else []

        if plot is not None:
            self.plot = plot
            self.points = points

    def resetDetails(self):

        self.plot = None
        self.plotForm = None
        self.coordinates = []
        self.points = []

    def isValidPlot(self):

        return self.plotForm is not None and self.plotForm.is_valid()

    def savePlotAndPoints(self):

        if self.plotForm is not None:
            self.plot = self.plotForm.savePlot()
        else:
            self.plot.save()

        self.setPoints()
        self.savePoints()

    def savePoints(self):

        if self.points is not None and self.plot is not None:
            Point.objects.filter(shape=self.plot.shape).delete()

            for point in self.points:
                point.save()

    def setPoints(self):

        if len(self.coordinates) > 0:
            setNum = 0

            for coordinateSet in self.coordinates:
                for coordinate in coordinateSet:
                    self.points.append(
                        Point(
                            shape=self.plot.shape,
                            set=setNum,
                            order=len(self.points),
                            lat=coordinate["lat"],
                            long=coordinate["lng"]
                        )
                    )
                setNum += 1

    def jsonify(self):

        json: str = ""

        if self.plot is not None:
            json = {
                "name": self.plot.name,
                "description": self.plot.description,
                "id": self.plot.id,
                "parent": self.plot.parent,
                "area": self.plot.shape.area,
                "points": [[point.lat, point.long] for point in self.points]
            }

        return json
