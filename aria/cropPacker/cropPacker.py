import numpy as np
from shapely.geometry import Point
from utilities.geometry.geometry import rotateAroundOrigin
from utilities.geometry.rectangle import Rectangle
from utilities.geometry.polygon import Polygon


def squarePacking(radius, rectangle):
    numberOfColumns = int(rectangle.width / (radius * 2))
    numberOfRows = int(rectangle.length / (radius * 2))

    totalWidth = numberOfColumns * 2 * radius
    totalLength = numberOfRows * 2 * radius

    lengthAdjustment = (rectangle.length - totalLength) / 2
    widthAdjustment = (rectangle.width - totalWidth) / 2

    coordinates = list()
    for row in range(numberOfRows):
        for column in range(numberOfColumns):
            coordinate = ((2 * row * radius) + radius + lengthAdjustment,
                          (2 * column * radius) + radius + widthAdjustment)
            coordinates.append(coordinate)

    return np.asarray(coordinates)


def trianglePacking(radius, rectangle):
    numberOfCropsInLongRow = int(rectangle.length / (2 * radius))
    numberOfCropsInShortRow = int((rectangle.length - radius) / (2 * radius))

    totalLength = radius * (numberOfCropsInLongRow + numberOfCropsInShortRow + 1)
    lengthAdjustment = (rectangle.length - totalLength) / 2

    capCoefficient = 2 - np.sqrt(3)
    cap = radius * capCoefficient

    widthOfOneRow = radius * np.sqrt(3)
    numberOfRows = (rectangle.width - cap) // widthOfOneRow
    numberOfShortRows = int(numberOfRows // 2)
    numberOfLongRows = int(numberOfRows - numberOfShortRows)

    totalWidth = cap + numberOfRows * widthOfOneRow
    widthAdjustment = (rectangle.width - totalWidth) / 2

    coordinates = list()
    for row in range(numberOfLongRows):
        for column in range(numberOfCropsInLongRow):
            coordinate = (
                (2 * column * radius) + radius + lengthAdjustment,
                (2 * widthOfOneRow * row) + radius + widthAdjustment
            )
            coordinates.append(coordinate)
    for row in range(numberOfShortRows):
        for column in range(numberOfCropsInShortRow):
            coordinate = (
                (2 * column * radius) + 2 * radius + lengthAdjustment,
                (2 * widthOfOneRow * row) + widthOfOneRow + radius + widthAdjustment
            )
            coordinates.append(coordinate)

    coordinates = np.asarray(coordinates)

    return coordinates


def packWithBestPackingScheme(radius, rectangle):
    square = squarePacking(radius, rectangle)
    triangle = trianglePacking(radius, rectangle)
    positions = square if len(square) >= len(triangle) else triangle

    return positions


def getAbsolutePositions(relativePositions, rectangle):
    if relativePositions.size == 0:
        return relativePositions

    if rectangle.isFallenOver:
        relativePositions = np.flip(relativePositions, 1)

    absolutePositions = rotateAroundOrigin(rectangle.baseAngle, relativePositions)
    absolutePositions = np.add(absolutePositions, rectangle.lowestPoint)

    return absolutePositions


def removePositionsOutsideBounds(positions, bounds):
    positionsOutsideBounds = []
    shape = Polygon(bounds)
    for position in positions:
        if not shape.contains(Point(position)):
            positionsOutsideBounds.append(position)

    return positionsOutsideBounds


def packArea(radius, plot):
    smallestBoundingRectangle = Rectangle(plot.smallestBoundingRectangleCoordinates)
    relativeCropPositions = packWithBestPackingScheme(radius, smallestBoundingRectangle)
    absoluteCropPositions = getAbsolutePositions(relativeCropPositions, smallestBoundingRectangle)

    return absoluteCropPositions
