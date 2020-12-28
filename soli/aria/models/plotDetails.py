import json

from django.shortcuts import get_object_or_404

from aria.forms.plot import PlotForm
from aria.models.farm import Farm
from aria.models.plot import Plot
from aria.models.point import Point


class PlotDetails:
    plot = None
    plotForm = None
    type = None
    coordinates = []
    points = []
    children = []
    owner = None
    farm = None

    def __init__(self, owner=None, farm=None, request=None, plot=None, points=None, children=None):

        self.resetDetails()

        if request is not None:
            plotId = request.POST.get("id")
            if plotId is not None:
                self.plot = get_object_or_404(Plot, id=plotId)

            self.plotForm = PlotForm(request.POST, instance=self.plot)
            self.coordinates = json.loads(request.POST["points"]) if "points" in request.POST else []
            self.type = request.POST["type"] if "type" in request.POST else None
            self.owner = request.user
            self.farm = Farm.objects.get(owner=self.owner)
        elif plot is not None:
            self.plot = plot
            self.type = plot.type

        if children:
            self.children = children

        if farm is not None:
            self.farm = farm

        if owner is not None:
            self.owner = owner

        self.points = points if points is not None else []

    def resetDetails(self):

        self.plot = None
        self.plotForm = None
        self.coordinates = []
        self.points = []
        self.children = []
        self.owner = None
        self.farm = None

    def isValidPlot(self):

        return self.plotForm is not None and self.plotForm.is_valid()

    def savePlotAndPoints(self):

        if self.plotForm is not None:
            self.plot = self.plotForm.savePlot(owner=self.owner, farm=self.farm)
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
            if self.points is None:
                self.points = []
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
                "parent": self.plot.parent.id if self.plot.parent else None,
                "area": self.plot.shape.area,
                "type": self.plot.type,
                "children": [child.jsonify() for child in self.children] if self.children else None,
                "points": [[point.lat, point.long] for point in self.points],
            }

        return json
