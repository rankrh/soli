from aria.models import Plot, Point


class PlotDetails():
    plot = None
    points = []

    def __init__(self, plt_num):
        self.plot = Plot.objects.filter(plt_num=plt_num).get()
        self.points = Point.objects.filter(pt_plt_num=plt_num).order_by("pt_order")

    def jsonify(self):
        return {
            "name": self.plot.plt_name,
            "num": self.plot.plt_num,
            "parent": self.plot.plt_parent_num,
            "points": [[point.pt_lat, point.pt_long] for point in self.points]
        }