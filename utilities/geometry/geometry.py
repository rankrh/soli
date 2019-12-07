import numpy as np

def getDistance(point1, point2):
    return np.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


def unitVector(vector):
    return vector / np.linalg.norm(vector)


def angleBetween(v1, v2):
    v1_u = unitVector(v1)
    v2_u = unitVector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def rotateAroundOrigin(angle, coordinates):
    newCoordinates = list()

    for coordinate in coordinates:
        x = coordinate[0] * np.cos(angle) - coordinate[1] * np.sin(angle)
        y = coordinate[1] * np.cos(angle) + coordinate[0] * np.sin(angle)

        newCoordinates.append((x, y))

    return newCoordinates

def getVector(point1, point2):

    return (point2[0] - point1[0], point2[1] - point1[1])
