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
