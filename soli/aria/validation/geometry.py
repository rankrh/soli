from functools import reduce
import operator
import math

def calculateDistance(pointA, pointB):
     distance = math.sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)  
     return distance

def orderCoordinates(*coords):
    if len(coords) == 0 or coords is None:
        return

    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
    return sorted(coords, key=lambda coord: (135 - math.degrees(-math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)


