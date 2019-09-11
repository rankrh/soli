from plot.plot import Plot

rectangle = Plot(
    crop="corn",
    shape="rectangle",
    topRight=(1, 1),
    topLeft=(0, 0),
    bottomLeft=(1, 2),
    bottomRight=(2, 1))

print(rectangle.crop)


