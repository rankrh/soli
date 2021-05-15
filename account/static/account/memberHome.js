L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

var maps = new Object();

$(document).ready(function() {
	loadMaps();
});

function loadMaps() {
	$("div[id^='farm-map-']").each(function() {
		var farm = $(this);
        let coordinates = getFarmCoordinates(farm);
        let valid = coordinatesAreValid(coordinates);

        let zoom = valid ? 16 : 4;
        coordinates = valid ? coordinates : [40, -100];

    	maps[farm.attr("data-farmId")] = L.mapbox.map(this)
			.setView(coordinates, zoom)
			.addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'));

	});
}

function getFarmCoordinates(farm) {

    return [farm.attr("data-lat"), farm.attr("data-long")]
}

function coordinatesAreValid(coordinates) {

    return coordinates.filter(x => x !== "").length == 2;
}