L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

var maps = new Object();

$(document).ready(function() {
	loadMaps();
});

function loadMaps() {
	$("div[id^='farm-map-']").each(function() {
		var farm = $(this);

		maps[farm.attr("data-farmId")] = L.mapbox.map(this)
			.setView(getFarmCoordinates(farm), 16)
			.addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'));

	});
}

function getFarmCoordinates(farm) {

	return [farm.attr("data-lat"), farm.attr("data-long")];
}