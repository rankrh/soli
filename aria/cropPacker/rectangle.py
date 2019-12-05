from polygon import Polygon
from geometry import getDistance, getVector
import numpy as np

class Rectangle(Polygon):
    def __init__(self, coordinates):
        ## TODO: Check if is rectangle
        super().__init__(coordinates)
        self.dimensions = self.getDimensions()
        self.length, self.width = max(self.dimensions), min(self.dimensions)
        self.lowestPoint = self.getLowestPoint()
        self.baseAngle = self.getBaseAngle()
        self.isFallenOver = self.checkIfFallenOver()
        
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
        lowestPoint = self.coordinates[0]

        for coordinate in self.coordinates:
            if coordinate[1] < lowestPoint[1]:
                lowestPoint = coordinate
        
        return lowestPoint
       
    def getDistanceToFurthestRightPoint(self):
    	return getDistance(self.lowestPoint, self.getPointCounterClockwise(self.lowestPoint))

    def getBaseAngle(self):
        
        baseVector = getVector(self.lowestPoint, self.getPointCounterClockwise(self.lowestPoint))
        baseAngle = baseVector[1] / baseVector[0]
        return np.arctan(baseAngle)


    def getDimensions(self):
        return (getDistance(self.coordinates[0], self.coordinates[1]),
                getDistance(self.coordinates[1], self.coordinates[2]))

    def checkIfFallenOver(self):
        return self.getDistanceToFurthestRightPoint() == self.width
