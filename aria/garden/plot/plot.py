from soli.services.geometry.Rectangle import Rectangle
from crop.cropPacker import packRectangle

class Plot:

    def placeCrops(self):

        return packRectangle(self.crop.radius, self.shape.coordinates)
    
    def getTotalYield(self):

        total = self.crop.yieldPerPlant * self.numberOfPlants
        return total
    
    def getGallonsPerWeek(self):

        water = self.crop.gallonsPerWeek * self.numberOfPlants
        return water
