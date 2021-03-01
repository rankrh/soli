
function addPolygon(map, name, coords) {

	map.addSource(
		name, {
			'type': 'geojson',
			'data': {
				'type': 'Feature',
				'geometry': {
					'type': 'Polygon',
					'coordinates': [coords]
				}
			}
		}
	);

	map.addLayer({
		'id': name,
		'type': 'fill',
		'source': name,
		'layout': {},
		'paint': {
			'fill-color': '#088',
			'fill-opacity': 0.8
		}
	});
}