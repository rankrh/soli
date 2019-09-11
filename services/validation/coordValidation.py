def validateCoordinates(*coordinates):
    for coordinate in coordinates:
        if not type(coordinate) == tuple:
            raise ValueError(
                "All coordinates must be of type tuple"
            )

    print(coordinates)
    return coordinates
