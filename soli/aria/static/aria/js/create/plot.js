mapboxgl.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

const plots = JSON.parse($("#plots-data").text());

var map = new mapboxgl.Map({
	container: 'map', // container id
	style: 'mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr', //hosted style id
	center: [-100, 40], // starting position
	zoom: 3 // starting zoom
});

var draw = new MapboxDraw({
	displayControlsDefault: false,
	controls: {
    polygon: true,
    polyline: false,
    rectangle: false,
    circle: false,
    marker: false
	}
});

var geocoder = new MapboxGeocoder({ // Initialize the geocoder
  accessToken: mapboxgl.accessToken, // Set the access token
  mapboxgl: mapboxgl, // Set the mapbox-gl instance
  marker: false, // Do not use the default marker style
});

map.addControl(geocoder);
map.addControl(draw);

map.on('draw.create', updateArea);
map.on('draw.delete', updateArea);
map.on('draw.update', updateArea);
map.on('load', function () { initializePlots() });

$("input[type=radio][name=units]").change(
	function() {
		for (i=0; i < plots.length; i++) {
			updateAreaUI(plots[i]);
		}
	}
);

function initializePlots() {

	addSavedPlots();
}

function updateArea(e) {

	var data = draw.getAll();
	if (data.features.length > 0) {
		var area = calculateArea(data);
		updateStoredArea(area);
		updateAreaUI();
	}
}

function updateAreaUI(plot) {

	var units = $("input[name='units']:checked");
	var convertedArea = convertArea(plot.area, units.val());

	$("#formatted-area-" + plot.num).text(convertedArea + " " + units.closest('label').text());
}

function updateStoredArea(area) {

	$("#calculated-area").val(area);
}

function calculateArea(data) {

	return roundTo2Decimals(turf.area(data));
}

function addSavedPlots() {

	for (i=0; i < plots.length; i++) {
		var plot = plots[i];
		addPolygon(map, plot.name, plot.points);
		updateAreaUI(plot);
	}
}
