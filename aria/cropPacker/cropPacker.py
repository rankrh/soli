import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull, KDTree
from scipy.ndimage.interpolation import rotate
from shapely.geometry import Point

class Polygon:
    def __init__(self, coordinates):
        self.coordinates = np.asarray(coordinates)
        self.pointClosestToOrigin = self.getPointClosestToOrigin()
    
    
    def getPointClosestToOrigin(self):
        return self.coordinates[KDTree(self.coordinates).query([0, 0])[1]]
        
    def smallestBoundingRectangle(self):
        """
        Find the smallest bounding rectangle for a set of points.
        Returns a set of points representing the corners of the bounding box.
        :param points: an nx2 matrix of coordinates
        :rval: an nx2 matrix of coordinates
        """
        pi2 = np.pi / 2.
    
        # get the convex hull for the points
        hull_points = self.coordinates[ConvexHull(self.coordinates).vertices]
    
        # calculate edge angles
        #edges = np.zeros((len(hull_points) - 1, 2))
        edges = hull_points[1:] - hull_points[:-1]
    
        #angles = np.zeros((len(edges)))
        angles = np.arctan2(edges[:, 1], edges[:, 0])
    
        angles = np.abs(np.mod(angles, pi2))
        angles = np.unique(angles)
    
        # find rotation matrices
        # XXX both work
        rotations = np.vstack([
            np.cos(angles),
            np.cos(angles - pi2),
            np.cos(angles + pi2),
            np.cos(angles)]).T
        #     rotations = np.vstack([
        #         np.cos(angles),
        #         -np.sin(angles),
        #         np.sin(angles),
        #         np.cos(angles)]).T
        rotations = rotations.reshape((-1, 2, 2))
    
        # apply rotations to the hull
        rot_points = np.dot(rotations, hull_points.T)
    
        # find the bounding points
        min_x = np.nanmin(rot_points[:, 0], axis=1)
        max_x = np.nanmax(rot_points[:, 0], axis=1)
        min_y = np.nanmin(rot_points[:, 1], axis=1)
        max_y = np.nanmax(rot_points[:, 1], axis=1)
    
        # find the box with the best area
        areas = (max_x - min_x) * (max_y - min_y)
        best_idx = np.argmin(areas)
    
        # return the best box
        x1 = max_x[best_idx]
        x2 = min_x[best_idx]
        y1 = max_y[best_idx]
        y2 = min_y[best_idx]
        r = rotations[best_idx]
    
        rval = np.zeros((4, 2))
        rval[0] = np.dot([x1, y2], r)
        rval[1] = np.dot([x2, y2], r)
        rval[2] = np.dot([x2, y1], r)
        rval[3] = np.dot([x1, y1], r)
    
        return Rectangle(rval)
    
    
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


class Rectangle(Polygon):
    def __init__(self, coordinates):
        ## TODO: Check if is rectangle
        super().__init__(coordinates)
        self.dimensions = getRectangleDimensions(coordinates)
        self.length, self.width = max(self.dimensions), min(self.dimensions)
        self.lowestPoint = self.getLowestPoint()
        
    def getPointClockwise(self, point=None):
        ## TODO: numpy index
        if point is None:
            point = self.pointClosestToOrigin
        index = self.coordinates.tolist().index(point.tolist())
        return self.coordinates[(index + 1) % 4]
    
    def getPointCounterClockwise(self, point=None):
        ## TODO: numpy index
        if point is None:
            point = self.pointClosestToOrigin
        index = self.coordinates.tolist().index(point.tolist())
        return self.coordinates[(index % 4) - 1]
    
    def getLowestPoint(self):
    
        return np.amin(self.coordinates, 0)
       
    def slopeOfBase(self):
        
        lowestPoint = self.getLowestPoint()
        rise = self.pointClosestToOrigin[1] - lowestPoint[1]
        run = self.pointClosestToOrigin[0] - lowestPoint[0]
        slope = rise / run
        return slope
    
    def getBaseAngle(self):
        vector = self.lowestPoint - self.pointClosestToOrigin
        angle = angleBetween(vector, [1, 0])
        return angle
       
def getHeightOfDoubleRow(radius):
    return radius * (1 + (np.sqrt(3) * 1.5))

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
    
    print(rectangle.lowestPoint)
    print(rectangle.pointClosestToOrigin)
    absolutePositions = np.add(relativePositions, rectangle.pointClosestToOrigin)
#    angle = rectangle.getBaseAngle()
#    absolutePositions = rotateAroundOrigin(angle, absolutePositions)

    return absolutePositions
    
    angle = rectangle.getBaseAngle()
    if rectangle.pointClosestToOrigin[0] > rectangle.getPointClockwise()[0]:
        print("HERE")
        angle = -angle - np.pi / 2
        relativePositions = relativePositions * [-1, -1]
    elif rectangle.pointClosestToOrigin[1] < rectangle.getPointCounterClockwise()[1]:
        print("HERE2")
        angle = -angle - np.pi / 2
        relativePositions = relativePositions * [1, -1]

    absolutePositions = rotateAroundOrigin(angle, relativePositions)
    absolutePositions = np.add(absolutePositions, rectangle.pointClosestToOrigin)

    return absolutePositions

def removePositionsOutsideBounds(positions, bounds):
    positionsOutsideBounds = []
    shape = Polygon(bounds)
    for position in positions:
        if not shape.contains(Point(position)):
            positionsOutsideBounds.append(position)

    return positionsOutsideBounds


def getDistance(point1, point2):
    return np.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


def getRectangleDimensions(coordinates):
    return (getDistance(coordinates[0], coordinates[1]),
            getDistance(coordinates[1], coordinates[2]))


def unitVector(vector):
    return vector / np.linalg.norm(vector)


def angleBetween(v1, v2):
    v1_u = unitVector(v1)
    v2_u = unitVector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def rotateAroundOrigin(angle, coordinates):
    newCoordinates = list()

    for coordinate in coordinates:
        x = np.cos(angle) * coordinate[0] + np.sin(angle) * coordinate[1]
        y = np.sin(angle) * -coordinate[0] + np.cos(angle) * coordinate[1]

        newCoordinates.append((x, y))

    return newCoordinates

def vectorBetween(point1, point2):
    return

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
    
    smallestBoundingRectangle = plot.smallestBoundingRectangle()
    relativeCropPositionss = packWithBestPackingScheme(radius, smallestBoundingRectangle)
    for relativeCropPositions in relativeCropPositionss:
        absoluteCropPositions = getAbsolutePositions(relativeCropPositions, smallestBoundingRectangle)
#    print(vectorBetween(smallestRectangleCoordinates[0], smallestRectangleCoordinates[1]))
#    #print(angleBetween(smallestRectangleCoordinates[0], (1, 0)))
#    #positions = rotatePlotAroundOrigin(angleBetween(smallestRectangleCoordinates[0], (1, 0)), positions)
#    
        createPlot(plot, smallestBoundingRectangle, absoluteCropPositions, radius, relativeCropPositions)


for i in range(1):
    points = np.random.rand(5, 2)
    plot = Polygon(points)
    packArea(0.05, plot)

#points = [[0.03226647618765244, 0.4366976148010131], [0.02474447461316287, 0.49633012975040525], [0.9256814554229232, 0.7096226610410066], [0.048568445776916325, 0.8929167924708235], [0.4234273643265204, 0.9306386157235763]]
#packArea(0.05, Polygon(points))