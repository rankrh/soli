from aria.models import Plot, Point

class PlotDetails():
    plot = None
    points = []

    def __init__(self, plt_num):
        self.plot = Plot.objects.filter(plt_num=plt_num).get()
        self.points = Point.objects.filter(pt_plt_num=plt_num)
