from .coordinateValidator import validateCoordinates
from soli.aria.garden.plot.crop.crop import Crop

def validatePlot(crop, shape, center, radius, coordinates):
    if shape not in ['circle', 'rectangle']:
        raise ValueError(
            'Invalid shape.  Valid shapes are "circle" or "rectangle"'
        )

    if shape == "circle":
        if radius is None:
            raise ValueError(
                'Missing radius'
            )
        validateCoordinates(center)
        
    elif shape == "rectangle":
        if len(coordinates) != 4:
            raise ValueError(
                f"You must provide 4 coordinates. Num provided: {len(coordinates)}"
            )
        validateCoordinates(*coordinates)

    