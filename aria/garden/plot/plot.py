from soli.services.validation.plotValidator import validatePlot
from soli.services.validation.coordinateValidator import orderCoordinates
from crop.cropPacker import packRectangle

class Plot:
    def __init__(
            self,
            crop,
            shape,
            center=None,
            radius=None,
            boundaries=None):
        
        validatePlot(crop, shape, center, radius, boundaries)

        self.shape = shape
        self.center = center
        self.boundaries = orderCoordinates(*boundaries)
        self.crop = crop
        self.cropPositions = self.placeCrops()
        self.numberOfPlants = len(self.cropPositions)
        self.totalYield = self.getTotalYield()
        self.gallonsPerWeek = self.getGallonsPerWeek()
        
    def placeCrops(self):

        if self.shape == "rectangle":
            return packRectangle(self.crop.radius, self.boundaries)
    
    def getTotalYield(self):

        total = self.crop.yieldPerPlant * self.numberOfPlants
        return total
    
    def getGallonsPerWeek(self):

        water = self.crop.gallonsPerWeek * self.numberOfPlants
        return water
