from aria.models import Plot, Point


class PlotDetails:
    plot = None
    points = []

    def __init__(self, plt_num):
        self.points = Point.objects.filter(pt_plt_num=plt_num).order_by("order")

        if self.points.exists():
            self.plot = self.points[0].pt_plt_num

    def jsonify(self):
        return {
            "name": self.plot.plt_name,
            "description": self.plot.plt_description,
            "num": self.plot.plt_num,
            "parent": self.plot.plt_parent_num,
            "area": self.plot.plt_area,
            "points": [[point.pt_lat, point.pt_long] for point in self.points]
        }

def getPlotDetailsForCurrentUser():
    pass