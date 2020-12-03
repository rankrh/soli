mapboxgl.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

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

map.on('load', function () {addPlot()});

function addPlot(plot) {

	map.addSource(
		'maine', {
			'type': 'geojson',
			'data': {
				'type': 'Feature',
				'geometry': {
					'type': 'Polygon',
					'coordinates': [[
						[-67.13734351262877, 45.137451890638886],
						[-66.96466, 44.8097],
						[-68.03252, 44.3252],
						[-69.06, 43.98],
						[-70.11617, 43.68405],
						[-70.64573401557249, 43.090083319667144],
						[-70.75102474636725, 43.08003225358635],
						[-70.79761105007827, 43.21973948828747],
						[-70.98176001655037, 43.36789581966826],
						[-70.94416541205806, 43.46633942318431],
						[-71.08482, 45.3052400000002],
						[-70.6600225491012, 45.46022288673396],
						[-70.30495378282376, 45.914794623389355],
						[-70.00014034695016, 46.69317088478567],
						[-69.23708614772835, 47.44777598732787],
						[-68.90478084987546, 47.184794623394396],
						[-68.23430497910454, 47.35462921812177],
						[-67.79035274928509, 47.066248887716995],
						[-67.79141211614706, 45.702585354182816],
						[-67.13734351262877, 45.137451890638886]
					]]
				}
			}
		}
	);

	map.addLayer({
		'id': 'maine',
		'type': 'fill',
		'source': 'maine',
		'layout': {},
		'paint': {
			'fill-color': '#088',
			'fill-opacity': 0.8
		}
	});
}