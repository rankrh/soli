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
	trash: true
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

$("input[type=radio][name=units]").change(
	function() {
		var area = 	$("#calculated-area").val();
		updateAreaUI(area);
	}
);

function updateArea(e) {
	var data = draw.getAll();
	console.log(data);
	if (data.features.length > 0) {
		var area = calculateArea(data);
		updateStoredArea(area);
		updateAreaUI(area);
	}
}

function updateAreaUI(area) {

	var units = $("input[name='units']:checked");
	var convertedArea = convertArea(area, units.val());

	$("#formatted-area").text(convertedArea + " " + units.closest('label').text());
}

function updateStoredArea(area) {

	$("#calculated-area").val(area);
}

function calculateArea(data) {

	return roundTo2Decimals(turf.area(data));
}

map.on('load', function () {addSavedPlots()});

function addSavedPlots() {

	for (i=0; i < plots.length; i++) {
		addPlot(plots[i]);
	}
}

function addPlot(plot) {

	map.addSource(
		plot.name, {
			'type': 'geojson',
			'data': {
				'type': 'Feature',
				'geometry': {
					'type': 'Polygon',
					'coordinates': [plot.points]
				}
			}
		}
	);

	map.addLayer({
		'id': plot.name,
		'type': 'fill',
		'source': plot.name,
		'layout': {},
		'paint': {
			'fill-color': '#088',
			'fill-opacity': 0.8
		}
	});
}