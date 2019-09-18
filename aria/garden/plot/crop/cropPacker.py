def packRectangle(radius, x, y):
	packs = {"triangle": trianglePacking(radius, x, y), "square": squarePacking(radius, x, y)}

	return packs

def trianglePacking(radius, x, y):
	longRowY = radius
	shortRowY = 1.464 * radius
	oneMoreRowY = 1.732 * radius

	longRowX = x // (2 * radius)
	remainder = x % (2 * radius)

	if remainder >= radius:
		shortRowX = longRowX
	else:
		shortRowX = longRowX - 1

	if y < (2 * radius):
		total = 0
		longRows = 0
		shortRows = 0
		rows = 0
	else:
		y -= (2 * radius)

		rows = y // oneMoreRowY + 1
		longRows = rows // 2 + 1
		shortRows = rows - longRows

		total = longRows * longRowX + shortRows * shortRowX
	return {"total":total, "numLongRows": longRows, "inLongRows": longRowX, "numShortRows": shortRows, "inShortRows": shortRowX, "numRows": rows}

def squarePacking(radius, x, y):
	row = x // (radius * 2)
	col = y // (radius * 2)

	total = row * col
	return {"total":total, "inLongRows": row, "numLongRows": col}

if __name__ == "__main__":
	print(packRectangle(0.5, 1, 10000))
