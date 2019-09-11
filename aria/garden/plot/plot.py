from services.validation.coordValidation import *


class Plot:
    def __init__(
            self,
            crop,
            shape,
            center=None,
            radius=None,
            topRight=None,
            topLeft=None,
            bottomLeft=None,
            bottomRight=None):

        if shape not in ['circle', 'rectangle']:
            raise ValueError(
                'Invalid shape.  Valid shapes are "circle" or "rectangle"'
            )

        self.shape = shape
        if self.shape == 'circle':
            if radius is None:
                raise ValueError(
                    'You must set the radius for circles'
                )

            if center is None or type(center) != tuple:
                raise ValueError(
                    'You must set the center coordinate for circles'
                )

            self.center = validateCoordinates(center)
            self.radius = radius

        else:
            if topRight is None or topLeft is None or bottomLeft is None or bottomRight is None:
                raise ValueError(
                    'You must set all four corners for rectangles'
                )
            self.topLeft, self.topRight, self.bottomRight, self.bottomLeft = validateCoordinates(topLeft, topRight, bottomRight, bottomLeft)
        self.crop = crop
