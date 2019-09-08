from plot import Plot

rectangle = Plot(
    crop="corn",
    shape="rectangle",
    topRight=(0, 0),
    topLeft=(1, 1),
    bottomLeft=(1, 2),
    bottomRight=(2, 1))

print(rectangle.crop)
