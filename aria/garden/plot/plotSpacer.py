from plot import Plot
from crop.crop import Crop

plot = Plot(
    crop=Crop(
        radius=1,
        gallonsPerWeek=1),
    shape="rectangle",
    boundaries=[(0, 0), (100, 0), (0, 100), (100, 100)])


print(plot.cropPositions)