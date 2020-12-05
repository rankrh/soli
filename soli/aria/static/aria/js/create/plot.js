L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

var temp = null;
const plots = JSON.parse($("#plots-data").text());

var map = L.mapbox.map('map')
    .setView([40, -100], 4)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'));

var featureGroup = L.featureGroup().addTo(map);

var drawControl = new L.Control.Draw({
  	edit: { featureGroup: featureGroup },
  	draw: {
    	polygon: true,
    	polyline: false,
    	rectangle: false,
    	circle: false,
    	marker: false
  	}
}).addTo(map);

map.on('draw:created', showPolygonArea);
map.on('draw:edited', showAllPolygonAreas);
map.on('click', function () { initializePlots() });

function initializePlots() {

	addSavedPlots();
}

function addSavedPlots() {

	for (i=0; i < plots.length; i++) {
		var plot = plots[i];
		console.log(plot.points)
		L.polygon([plot.points]).addTo(map);
	}
}

function showAllPolygonAreas(map) {
 	map.layers.eachLayer(function(layer) {
 		showPolygonArea({ layer: layer });
 	});
 	temp = map;
}

function showPolygonArea(plot) {

	var area = (LGeo.area(plot.layer)).toFixed(2);

	$("#calculated-area").val(area);
  	featureGroup.addLayer(plot.layer);
  	plot.layer.bindPopup(area + ' m<sup>2</sup>');
  	plot.layer.openPopup();
}
