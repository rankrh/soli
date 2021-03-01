var headquarters;

var drawControl = new L.Control.Draw({
  	draw: {
    	polygon: false,
    	polyline: false,
    	rectangle: false,
    	circle: false,
    	marker: true
  	}
}).addTo(map);

map.on('draw:created', function (e) {
	updateFarmHeadquarters(e.layer);
	updateFarmClimate();
});

function updateFarmHeadquarters(marker) {

	if (headquarters) {
		map.removeLayer(headquarters);
	}

	marker.addTo(map);
	headquarters = marker;
	var latLng = headquarters.getLatLng();
	$("#id_location").val([latLng.lat, latLng.lng]);
}

function updateFarmClimate() {


}