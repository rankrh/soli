from functools import reduce
import operator
import math

def validateCoordinates(*coordinates):
    for coordinate in coordinates:
        if not type(coordinate) == tuple:
            raise ValueError(
                f"All coordinates must be of type tuple: {coordinate}"
            )
        for dimension in coordinate:
            if dimension < 0:
                raise ValueError(
                    f"All coordinates must be of type tuple: {coordinate}"
                )

    return coordinates

def orderCoordinates(*coords):
    if len(coords) == 0 or coords is None:
        return

    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
    return sorted(coords, key=lambda coord: (135 - math.degrees(-math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)