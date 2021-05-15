L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

var maps = new Object();

$(document).ready(function() {
	loadMaps();
});

function loadMaps() {
	$("div[id^='farm-map-']").each(function() {
		var farm = $(this);

        coordinates = getFarmCoordinates(farm);
        zoom = getZoom(coordinates);

    	maps[farm.attr("data-farmId")] = L.mapbox.map(this)
			.setView(coordinates, zoom)
			.addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'));

	});
}

function getZoom(coordinates) {

    return coordinates == [40, -100] ? 4 : 16;
}

function getFarmCoordinates(farm) {

    coordinates = [farm.attr("data-lat"), farm.attr("data-long")]

    if (!coordinates) {
        coordinates = [40, -100];
    }

	return coordinates;
}