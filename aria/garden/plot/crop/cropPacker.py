from .crop import Crop

def packCircle(plotRadius, cropRadius):

    cropToPlot = cropRadius / plotRadius

    if cropToPlot < 1:
        return None
    elif cropToPlot < 2:
        return 1
    elif cropToPlot < 2.154:
        return 2
    elif cropToPlot < 2.414:
        return 3
    elif cropToPlot < 2.701:
        return 4
    elif cropToPlot < 3:
        return 5
    elif cropToPlot < 3.304:
        return 7
    elif cropToPlot < 3.613:
        return 8
    elif cropToPlot < 3.813:
        return 9
    elif cropToPlot < 3.923:
        return 10
    elif cropToPlot < 4.029:
        return 11
    elif cropToPlot < 4.236:
        return 12
    elif cropToPlot < 4.328:
        return 13
    elif cropToPlot < 4.521:
        return 14
    elif cropToPlot < 4.615:
        return 15
    elif cropToPlot < 4.792:
        return 16
    elif cropToPlot < 4.863:
        return 17
    elif cropToPlot < 5.122:
        return 19
    elif cropToPlot < 6:
        return 20
    else:
        return None