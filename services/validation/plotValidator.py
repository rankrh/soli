from .geometryValidator import validateGeometry

def validatePlot(crop, shape, center, radius, coordinates):
    validateGeometry(shape, center, radius, coordinates)
