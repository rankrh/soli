import random
from crop.crop import Crop
from plot import Plot


def generateTestCrop():
    
    crop = Crop(
            radius=random.triangular(1, 24),
            gallonsPerWeek=random.randrange(1, 12),
            height=random.randrange(12, 72),
            yieldPerPlant=random.randrange(1, 100),
            name=random.choice(['corn', 'squash', 'beans']))
    
    return crop

def createCoordinates(width, height):
    
    return [(0, 0), (0, height), (width, height), (width, 0)]

def generateTestPlot():
    plots = list()
    for i in range(random.randrange(4, 10)):
        
        crop = generateTestCrop()
        
        plot = Plot(crop, createCoordinates(random.randrange(15, 1200), random.randrange(15, 1200)))
        plots.append(plot)
        
    return plots