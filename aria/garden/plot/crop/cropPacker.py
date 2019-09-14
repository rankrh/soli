def packCircle(numCircles, circleRadius):
	smallToLarge = {
		1: 1, 2:2, 3: 2.154, 4: 2.414, 5: 2.701, 6: 3, 7: 3, 8: 3.304, 9: 3.613,
		10: 3.813, 11: 3.923, 12:4.029, 13: 4.236, 14: 4.328, 15: 4.521,
		16: 4.615, 17: 4.792, 18: 4.792, 19: 4.863, 20: 5.122}

	if numCircles <= 20:
		return smallToLarge[circles] * circleRadius
	else:
		return


def packRectangle(numCircles, circleRadius, widthToHeight):
	x = (numCircles * widthToHeight).round()
	y = numCircles / x
