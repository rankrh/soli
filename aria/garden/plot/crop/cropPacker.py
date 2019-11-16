import numpy as np


def packRectangle(radius, coordinates, angle=None):
    
    length, width = getDimensions(coordinates)
    square = squarePacking(radius, length, width)
    triangle = trianglePacking(radius, length, width)
    
    pack = square if len(square) >= len(triangle) else triangle
    
    return rotatePlot(pack, angle)


def getDimensions(coordinates):

    length = np.sqrt((coordinates[1][0] - coordinates[0][0]) ** 2 + (coordinates[1][1] - coordinates[0][1]) ** 2)
    width =  np.sqrt((coordinates[3][0] - coordinates[0][0]) ** 2 + (coordinates[3][1] - coordinates[0][1]) ** 2)

    return length, width


def squarePacking(radius, x, y):
    if x < y:  x, y = y, x

    rows = int(x // (radius * 2))
    cols = int(y // (radius * 2))

    coordinates = list()
    for r in range(rows):
        for c in range(cols):
            coordinate = ((2 * r * radius) + radius, (2 * c * radius) + radius)
            coordinates.append(coordinate)

    return np.round(np.asarray(coordinates), 1)


def trianglePacking(radius, x, y):
    if x < y:
        x, y = y, x

    longX = int(x // (2 * radius))
    shortX = int((x - radius) // (2 * radius))

    doubleRows = int((y - (1.732 * radius)) // (3.464 * radius))
    remainder = y- (doubleRows * 3.464 * radius)
    longY = shortY = doubleRows
    if remainder >= (2 * radius):
        longY += 1

    coordinates = list()
    
    # Long row coords
    for r in range(longX):
        for c in range(longY):
            coordinate = ((2 * r * radius) + radius, (3.732 * c * radius) + radius)
            coordinates.append(coordinate)
    
    # Short rows coords
    for r in range(shortX):
        for c in range(shortY):
            coordinate = ((2 * r * radius) + 2 * radius, (3.732 * c * radius) + 3 * radius)
            coordinates.append(coordinate)

    return np.round(np.asarray(coordinates), 1)

def rotatePlot(coordinates, angle):

    if angle is None:
        return coordinates

    angle = angle * np.pi / 180
    newCoordinates = list()
    
    for coordinate in coordinates:
        x = np.cos(angle) * coordinate[0] - np.sin(angle) * coordinate[1]
        y = np.sin(angle) * coordinate[0] - np.cos(angle) * coordinate[1]
        
        newCoordinates.append((x, y))
        
    return np.round(newCoordinates, 1)
