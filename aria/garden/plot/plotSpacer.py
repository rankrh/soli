from generateTestPlot import generateTestPlot
from soli.aria.garden.garden import Garden

plots = generateTestPlot()

plots.sort(key=lambda plot: plot.crop.height, reverse=True)
for plot in plots:
    print(plot.crop.height)

