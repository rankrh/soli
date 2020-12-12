L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

const plots = JSON.parse($("#plots-data").text());

var map = L.mapbox.map('map')
    .setView([40, -100], 4)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'))
    .addControl(L.mapbox.geocoderControl('mapbox.places'));

var featureGroup = L.featureGroup().addTo(map);

function addSavedPlots() {

	var units = $("input[type=radio][name=units]:checked");
	for (i=0; i < plots.length; i++) {
		var plot = plots[i];
		var plotLayer = L.polygon([plot.points]);

		plotLayer._leaflet_id = plot.id;
		plotLayer.name = plot.name;
		plotLayer.addTo(map);

	  	featureGroup.addLayer(plotLayer);
	}

	updateAllPolygonAreas();
}


function updateAllPolygonAreas() {

	var units = $("input[type=radio][name=units]:checked");

 	featureGroup.eachLayer(function(layer) {
 		updatePolygonArea(layer);
 		updatePolygonPopup(layer, units);
 	});
}

function updatePolygonArea(plot) {

	plot.area = LGeo.area(plot);
}

function updatePolygonPopup(plot, units) {

	var convertedArea = convertArea(plot.area, units.val());
	var name = plot.name ? plot.name : "Unnamed Plot"
	var unitName = units.closest('label').text();
	unitName = unitName ? unitName : "acres";

  	var popUpMessage = "<b>" + name + "</b><br>" + convertedArea + ' ' + unitName;

  	plot.bindPopup(popUpMessage);
}

function zoomToBounds(boundedLayer) {

	if (boundedLayer) {
		map.fitBounds(boundedLayer.getBounds());
	}
}

function isMarkerInPlot(marker, plot) {

    var points = plot.getLatLngs();
    var x = marker.getLatLng().lat, y = marker.getLatLng().lng;

    var inside = false;
    for (var i = 0, j = points.length - 1; i < points.length; j = i++) {
        var xi = points[i].lat, yi = points[i].lng;
        var xj = points[j].lat, yj = points[j].lng;

        var intersect = ((yi > y) != (yj > y))
            && (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
        if (intersect) inside = !inside;
    }

    return inside;
};
