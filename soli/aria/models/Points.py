import json

from aria.models import Point


def getPointsList(request):

    try:
        points = json.loads(request["points"])
    except:
        points = []

    return points


class Points:

    points = []
    plot = None

    def __init__(self, request, plot=None):

        self.plot = plot
        self.setPoints(getPointsList(request))

    def setPoints(self, points):

        setNum = 0

        for pointSet in points:

            for point in pointSet:
                self.points.append(
                    Point(
                        pt_plt_num=self.plot,
                        pt_set=setNum,
                        pt_order=len(self.points),
                        pt_lat=point["lat"],
                        pt_long=point["lng"]
                    )
                )

            setNum += 1

    def savePoints(self):

        for point in self.points:
            point.save()

    def areAllValid(self):

        valid = len(self.points) > 0
        if valid:
            for point in self.points:
                if not point.is_valid():
                    valid = False
                    break

        return valid
