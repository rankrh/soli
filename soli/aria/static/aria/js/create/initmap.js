L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

const plots = JSON.parse($("#plots-data").text());

var map = L.mapbox.map('map')
    .setView([40, -100], 4)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'))
    .addControl(L.mapbox.geocoderControl('mapbox.places'));

var basePlots = L.featureGroup().addTo(map);
var subdivisions = L.featureGroup().addTo(map);

function addSavedPlots() {

	var units = $("input[type=radio][name=units]:checked");
	for (i=0; i < plots.length; i++) {
		var plot = plots[i];
		var plotLayer = L.polygon([plot.points]);

		plotLayer._leaflet_id = plot.id;
		plotLayer.name = plot.name;
		plotLayer.parent = plot.parent;
		plotLayer.addTo(map);

		if (plotLayer.parent) {
			plotLayer.setStyle({fillColor: '#11a033', fillOpacity:0.5, color:"#074215"});
			subdivisions.addLayer(plotLayer);
		} else {
	  		basePlots.addLayer(plotLayer);
		}
	}

	updateAllPolygonAreas();
}

function updateAllPolygonAreas() {

	var units = $("input[type=radio][name=units]:checked");

	updateBasePlotAreas(units);
	updateSubPlotAreas(units);
}

function updateBasePlotAreas(units) {
 	basePlots.eachLayer(function(layer) {
 		updatePolygonArea(layer);
 		updatePolygonPopup(layer, units);
 	});
}

function updateSubPlotAreas(units) {
 	subdivisions.eachLayer(function(layer) {
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

function lineInsidePlot(A, B, plot) {

	var inPlot = true;
	if (A && B && plot) {
		var line = turf.lineString([[A.getLatLng().lat, A.getLatLng().lng], [B.getLatLng().lat, B.getLatLng().lng]]);
		var plot = turf.polygon(currentPlot.toGeoJSON().geometry.coordinates);
		inPlot = turf.lineIntersect(line, plot) == 0;
	}

	return inPlot;
}


function deletePlot(plot) {
	deletePlots([plot]);
}

function deletePlots(plots) {

	$.ajax({
		type: "POST",
		url: "ajax/delete-plots",
		dataType: "json",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			plots: JSON.stringify(plots)
		},
		success: function(data) {
			for (var i = 0; i < plots.length; i++) {
				deletePlotAccordion(plots[i]);
			}
		}
	});
}