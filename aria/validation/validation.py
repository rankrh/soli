

def validateCoordinates(*coordinates):
    for coordinate in coordinates:
        if not type(coordinate) == tuple:
            raise ValueError(
                f"All coordinates must be of type tuple: {coordinate}"
            )
        for dimension in coordinate:
            if dimension < 0:
                raise ValueError(
                    "All coordinates must be positive"
                )

def validateRectangle(coordinates):
    if len(coordinates) != 4:
        raise ValueError(
            f"You must provide 4 coordinates. Num provided: {len(coordinates)}"
        )

    validateCoordinates(*coordinates)    

 
def validateCircle(radius, center):
    if radius is None:
        raise ValueError(
            'Missing radius'
        )

    validateCoordinates(center)

