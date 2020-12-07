L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

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

map.on('draw:created', function (e) {
	var plot = e.layer;

	persistPlot(plot);
	createPlotAccordion(plot);
	featureGroup.addLayer(plot);
	editPlotDetails(plot);
});

map.on('draw:edited', updateAllPolygonAreas);
$(initializePlots());
$("input[type=radio][name=units]").change(
	function() {
		updateAllPolygonAreas();
	}
);

function initializePlots() {

	addSavedPlots();
	zoomToBounds(featureGroup);
}

function zoomToBounds(boundedLayer) {

	map.fitBounds(boundedLayer.getBounds());
}

function editPlotDetails(plot) {

	$("#edit-plot-id").val(plot.id);

	if (plot.name) {
		$("#edit-plot-name").val(plot.name)
	}

	if (plot.description) {
		$("#edit-plot-description").val(plot.description)
	}

	$("#edit-plot-modal").modal("toggle");
}

function savePlotDetails() {

	var plotNum = $("#edit-plot-id").val();
	var plot = featureGroup.getLayer(plotNum);

	plot.name = $("#edit-plot-name").val();
	plot.description = $("#edit-plot-description").val();
	persistPlot(plot);
	updatePlotAccordion(plot);
	updatePolygonArea(plot);
	clearEditPlotModal();
}

function persistPlot(plot) {

	$.ajax({
		type: "POST",
		url: "ajax/plot",
		dataType: "json",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			plt_num: plot.id,
			plt_name: plot.name,
			plt_description: plot.description,
			points: JSON.stringify(plot.getLatLngs())
		}
	});
}

function createPlotAccordion(plot) {
}

function updatePlotAccordion(plot) {

	$("#plot-" + plotNum + "-name").val(plot.name);
	$("#plot-" + plotNum + "-description").val(plot.description);
}

function clearEditPlotModal() {

	$("#edit-plot-modal").modal("toggle");
	$("#edit-plot-name").val("");
	$("#edit-plot-description").val("");
}

function addSavedPlots() {

	var units = $("input[type=radio][name=units]:checked");
	for (i=0; i < plots.length; i++) {
		var plot = plots[i];
		var plotLayer = L.polygon([plot.points]);

		plotLayer._leaflet_id = plot.num;
		plotLayer.name = plot.name;
		plotLayer.addTo(map);

	  	featureGroup.addLayer(plotLayer);
		updatePolygonAreaPopup(plotLayer, units);
	}
}

function updateAllPolygonAreas(map) {

	var units = $("input[type=radio][name=units]:checked");

 	featureGroup.eachLayer(function(layer) {
 		updatePolygonArea(layer, units);
 	});
}

function updatePolygonArea(plot, units) {

	if (!units) {
		units = $("input[type=radio][name=units]:checked");
	}

	updatePolygonAreaPopup(plot, units);
  	plot.openPopup();
}

function updatePolygonAreaPopup(plot, units) {

	var area = convertArea(LGeo.area(plot), units.val());
	var name = plot.name ? plot.name : "Unnamed Plot"
  	var popUpMessage = "<b>" + name + "</b><br>" + area + ' ' + units.closest('label').text();

  	plot.bindPopup(popUpMessage);
}
