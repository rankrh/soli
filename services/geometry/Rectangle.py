from soli.services.validation.geometryValidator import validateRectangle
from soli.services.validation.geometryValidator import orderCoordinates
from soli.services.validation.geometryValidator import calculateDistance

class Rectangle:
    coordinates = None
    area = None
    length = None
    width = None
    
    def __init__(self, coordinates):
        validateRectangle(coordinates)
        self.coordinates = orderCoordinates(*coordinates)

        self.length = self.getLength()
        self.width = self.getWidth()       
        self.area = self.getArea()
        
    def getLength(self):
        if self.coordinates is not None:
            return calculateDistance(self.coordinates[0], self.coordinates[1])
        else:
            raise ValueError("Coordinates must not be None")
    
    def getWidth(self):
        if self.coordinates is not None:
            return calculateDistance(self.coordinates[1], self.coordinates[2])
        else:
            raise ValueError("Coordinates must not be None")
        
    def getArea(self):
        try:
            return self.length * self.width
        except:
            raise ValueError("Length or width undefined")
        