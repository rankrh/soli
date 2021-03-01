import numpy as np
import pandas as pd
from shapely.geometry import Point

from soli.utilities.geometry.geometry import rotateAroundOrigin
from soli.utilities.geometry.polygon import Polygon
from soli.utilities.geometry.rectangle import Rectangle
from soli.utilities.math.general import getGoldenestFactor, getDivisorsAndRemainders


# from utilities.geometry.geometry import rotateAroundOrigin
# from utilities.geometry.rectangle import Rectangle
# from utilities.geometry.polygon import Polygon


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


def isPlotTooLong(squarestFactor):
    print(squarestFactor[0] / squarestFactor[1])
    return


def findAreaToPack(crop, numberOfCrops):
    factors = getFactorPairs(numberOfCrops)
    nextLargestNumberOfCrops = numberOfCrops + 1

    if len(factors) == 0:
        return

    while len(factors) == 1:
        factors = getFactorPairs(nextLargestNumberOfCrops)
        nextLargestNumberOfCrops += 1

    squarestFactor = factors[-1]
    goldenestFactor = getGoldenestFactor(factors)

    print(goldenestFactor)


## 1. find square packing arrangement with least area
#### this will be the arrangement(s) with the fewest number of wasted spaces
##
## 2. find triangle packing arrangement with the least area
#### this will be the arrangement(s) with the fewest number of wasted spaces
#### AND the "squarest" arrangement
## 
## 3. compare the two arrangements and choose the one with the lowest area
## 4. fill in wasted space(s) and compute new crop totals

## Restrictions:
## The width cannot exceed 4ft

garden = [10, 20]


def getPerimeter(squarePacking):
    return 2 * squarePacking.rows + 2 * squarePacking.cols


def getSquarePackedArea(plots, radius, walkwayWidth):
    areaOfOneCrop = (radius * 2) ** 2
    return plots.rows * (plots.cols + (
                plots.remainder > 0)) * areaOfOneCrop + walkwayWidth * plots.perimeter + 4 * walkwayWidth ** 2


def getSquarePackingAreaData(numberOfCrops, radius):
    squarePacking = pd.DataFrame(
        getDivisorsAndRemainders(numberOfCrops),
        columns=['rows', 'cols', 'remainder'])

    squarePacking[['length', 'width']] = squarePacking[['rows', 'cols']] * radius * 2
    squarePacking['perimeter'] = getPerimeter(squarePacking)
    squarePacking['area'] = getSquarePackedArea(squarePacking, radius, 1)
    return squarePacking.loc[squarePacking.area.idxmin()][['length', 'width', 'perimeter', 'area']]


def getHalfFactors(x):
    halfFactors = []

    for i in np.arange(1.5, int(np.sqrt(x)) + 1, 0.5):
        longRow = int(i)

        if i % 1 == 0:
            shortRow = longRow - 1
        else:
            shortRow = longRow

        columns = 0
        numberOfCropsLeft = x

        while numberOfCropsLeft > 0:
            if columns % 2 == 0:
                numberOfCropsLeft -= longRow
            else:
                numberOfCropsLeft -= shortRow

            columns += 1
        remainder = abs(numberOfCropsLeft)

        halfFactors.append((longRow, shortRow, columns, remainder))

    return np.array(halfFactors)


def getTrianglePackingAreaData(numberOfCrops, radius):
    trianglePacking = pd.DataFrame(
        getHalfFactors(numberOfCrops),
        columns=["longRow", "shortRow", "cols", "remainder"])

    widthOfOneRow = radius * np.sqrt(3)
    capCoefficient = 2 - np.sqrt(3)
    cap = radius * capCoefficient

    trianglePacking["length"] = radius * 2 * trianglePacking.longRow + (
                1 - (trianglePacking.longRow - trianglePacking.shortRow)) * radius
    trianglePacking["width"] = (widthOfOneRow * trianglePacking.cols) + cap
    return trianglePacking


def getSmallestArea(numberOfCrops, radius):
    # squareAreas = getSquarePackingAreaData(numberOfCrops, radius)
    triangleAreas = getTrianglePackingAreaData(numberOfCrops, radius)

    return triangleAreas


# for x in range(1, 21):
#    print(x)
#    print(getSmallestArea(x, 0.5))
#    print()

print(getSmallestArea(20, 0.5))
