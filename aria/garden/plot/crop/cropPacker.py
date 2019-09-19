def packRectangle(radius, x, y):

	packs = [squarePacking(radius, x, y), trianglePacking(radius, x, y)]
	
	return packs

def squarePacking(radius, x, y):

	rows = int(x // (radius * 2))
	cols = int(y // (radius * 2))

	total = rows * cols
	coordinates = list()
	for x in range(rows):
		for y in range(cols):
			coordinate = ((2 * x * radius) + radius, (2 * y * radius) + radius)
			coordinates.append(coordinate)

	return {"total":total} #, "coordinates": coordinates}

def trianglePacking(radius, x, y):
	if x < y:
		x, y = y, x

	longX = int(x // (2 * radius))
	shortX = int((x - radius) // (2 * radius))

	doubleRows = int((y - 1.732) // (3.464 * radius))
	remainder = y- (doubleRows * 3.464 * radius)
	longY = shortY = doubleRows
	if remainder >= (2 * radius):
		longY += 1

	total = longX * longY + shortX * shortY

	coordinates = list()

	return {"total": total} #, "coordinates": coordinates}



if __name__ == "__main__":
	print(packRectangle(3.5, 27, 700))
