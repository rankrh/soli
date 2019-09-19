from .geometryValidator import validateGeometry
from soli.aria.garden.plot.crop.crop import Crop

def validatePlot(crop, shape, center, radius, coordinates):
    validateGeometry(shape, center, radius, coordinates)
    
    if not type(crop) == type(Crop):
        raise ValueError("Crop must be of type Crop")
