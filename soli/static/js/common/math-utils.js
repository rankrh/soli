function convertArea(area, returnUnit) {

	var convertedArea = 0;
	if (!returnUnit || returnUnit === "acres") {
		convertedArea = meters2ToAcres(area);
	} else if (returnUnit === "meters") {
		convertedArea = area;
	} else if (returnUnit === "miles") {
		convertedArea = meters2ToMiles2(area);
	} else if (returnUnit === "hectares") {
		convertedArea = meters2ToHectares(area);
	} else {
		console.log(area);
		console.log(returnUnit);
	}

	return roundTo2Decimals(convertedArea);
}

function meters2ToAcres(area) {

	return area * 2471 * 0.0000001;
}

function meters2ToHectares(area) {

	return area * 0.0001;
}

function meters2ToMiles2(area) {

	return area * 3671 * 0.0000000001;
}

function roundTo2Decimals(number) {

	return Math.round(number * 100) / 100;
}