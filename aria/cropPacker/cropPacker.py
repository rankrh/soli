import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import rotate
from shapely.geometry import Point
from polygon import Polygon
from rectangle import Rectangle
from geometry import rotateAroundOrigin
    
def squarePacking(radius, rectangle):

    numberOfColumns = int(rectangle.width / (radius * 2))
    numberOfRows = int(rectangle.length / (radius * 2))
    
    totalLength = numberOfColumns * 2 * radius
    lengthAdjustment = (rectangle.length - totalLength) / 2
    
    totalWidth = numberOfRows * 2 * radius
    widthAdjustment = (rectangle.width - totalWidth) / 2

    coordinates = list()
    for row in range(numberOfRows):
        for column in range(numberOfColumns):
            coordinate = ((2 * row * radius) + radius, (2 * column * radius) + radius)
            coordinates.append(coordinate)
            
    return np.asarray(coordinates)

def getRowWidth(radius):
    return 2 * radius * np.sqrt(3)
        
def trianglePacking(radius, rectangle):
    
    numberOfCropsInLongRow = int(rectangle.length / (2 * radius))
    numberOfCropsInShortRow = int((rectangle.length - radius) / (2 * radius))
    
    widthOfOneRow = getRowWidth(radius)    
    cap = (2 * radius) - widthOfOneRow
    numberOfLongRows = int((rectangle.width - cap) / widthOfOneRow)
    numberOfShortRows = int(rectangle.width / widthOfOneRow)

    coordinates = list()
    for row in range(numberOfLongRows):
        # Long row coords
        for column in range(numberOfCropsInLongRow):
            coordinate = (
                    (2 * column * radius) + radius,
                    (widthOfOneRow * row) + radius
                )
            coordinates.append(coordinate)
    for row in range(numberOfShortRows):
        for column in range(numberOfCropsInShortRow):
            coordinate = (
                    (2 * column * radius) + 2 * radius,
                    (widthOfOneRow * row) + widthOfOneRow / 2 + radius
                )
            coordinates.append(coordinate)
            
    coordinates = np.asarray(coordinates)
    return coordinates


def packWithBestPackingScheme(radius, rectangle):
    square = squarePacking(radius, rectangle)
    triangle = trianglePacking(radius, rectangle)
    positions = square if len(square) >= len(triangle) else triangle
    return [square, triangle]

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

def createPlot(plot, rectangle, absolutePositions, radius, relativeCropPositions):
    if len(absolutePositions) == 0:
        return
#    plt.scatter(plot.coordinates[:, 0], plot.coordinates[:, 1])
    plt.fill(rectangle.coordinates[:, 0], rectangle.coordinates[:, 1], alpha=0.2)
#    plt.scatter(rectangle.pointClosestToOrigin[0], rectangle.pointClosestToOrigin[1], color='green')
#    plt.scatter(rectangle.getPointClockwise()[0], rectangle.getPointClockwise()[1], color="red")
    ax = plt.gcf().gca()
    for position in absolutePositions:
        ax.add_artist(plt.Circle(position, radius, alpha=0.3))
#    for position in relativeCropPositions:
#        ax.add_artist(plt.Circle(position, radius, alpha=0.3, color='black'))

    plt.axis('equal')
    plt.show()


def packArea(radius, plot):
    
    smallestBoundingRectangle = Rectangle(plot.smallestBoundingRectangleCoordinates)
    relativeCropPositionss = packWithBestPackingScheme(radius, smallestBoundingRectangle)
    for relativeCropPositions in relativeCropPositionss:
        absoluteCropPositions = getAbsolutePositions(relativeCropPositions, smallestBoundingRectangle)
#    print(vectorBetween(smallestRectangleCoordinates[0], smallestRectangleCoordinates[1]))
#    #print(angleBetween(smallestRectangleCoordinates[0], (1, 0)))
#    #positions = rotatePlotAroundOrigin(angleBetween(smallestRectangleCoordinates[0], (1, 0)), positions)
#    
        createPlot(plot, smallestBoundingRectangle, absoluteCropPositions, radius, relativeCropPositions)


for i in range(2):
    points = np.random.rand(5, 2)
    plot = Polygon(points)
    packArea(0.05, plot)

#points = [[0.03226647618765244, 0.4366976148010131], [0.02474447461316287, 0.49633012975040525], [0.9256814554229232, 0.7096226610410066], [0.048568445776916325, 0.8929167924708235], [0.4234273643265204, 0.9306386157235763]]
#packArea(0.05, Polygon(points))