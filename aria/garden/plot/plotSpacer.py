from plot import Plot
from crop.crop import Crop

corn = Crop(
    radius=6,
    gallonsPerWeek=1,
    height=72,
    yieldPerPlant=64)

plot = Plot(
    crop=corn,
    shape="rectangle",
    boundaries=[(0, 0), (120, 120), (0, 120), (120, 0)])

print(plot.totalYield)
print(plot.gallonsPerWeek)