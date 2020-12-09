L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

const plots = JSON.parse($("#plots-data").text());

var map = L.mapbox.map('map')
    .setView([40, -100], 4)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'))
    .addControl(L.mapbox.geocoderControl('mapbox.places'));

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

	updatePolygonArea(plot);
	persistPlot(plot);
	editPlotDetails(plot);
});

map.on('draw:edited', function (e) {
	e.layers.eachLayer(function(layer) {
		updatePolygonArea(layer);
		persistPlot(layer);
	});
	updateAllPolygonAreas();
});

map.on('draw:deleted', function (e) {

	var plotsToDelete = []

	e.layers.eachLayer(function(layer) {
		plotsToDelete.push(layer._leaflet_id)
	});

	deletePlots(plotsToDelete);
});

$(initializePlots());

$("input[type=radio][name=units]").change(
	function() {
		updateAllPolygonAreas();
	}
);

function initializePlots() {

	addSavedPlots();
	zoomToBounds(featureGroup);
	updateAllPolygonAreas();
}

function togglePlotFocus(plotId) {

	var boundedLayer = featureGroup;
	if (!$("#collapse-plot-" + plotId).hasClass("show")) {
		boundedLayer = featureGroup.getLayer(plotId);
		boundedLayer.openPopup();
	}

	zoomToBounds(boundedLayer);
}

function zoomToBounds(boundedLayer) {

	if (boundedLayer) {
		map.fitBounds(boundedLayer.getBounds());
	}
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

	var plot = featureGroup.getLayer(Number($("#edit-plot-id").val()));

	plot.name = $("#edit-plot-name").val();
	plot.description = $("#edit-plot-description").val();

	persistPlot(plot);
	updatePlotAccordion(plot);
	updatePolygonArea(plot);
	updatePolygonPopup(plot, $("input[type=radio][name=units]:checked"))
	clearEditPlotModal();
}

function persistPlot(plot) {

	$.ajax({
		type: "POST",
		url: "ajax/plot",
		dataType: "json",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			id: plot._leaflet_id,
			name: plot.name,
			description: plot.description,
			area: plot.area,
			points: JSON.stringify(plot.getLatLngs())
		},
		success: function(data) {
			$("#edit-plot-id").val(data.plot);
			plot._leaflet_id = data.plot;
			featureGroup.addLayer(plot);

			if ($("#plot-details-" + plot._leaflet_id).length == 0) {
				createPlotAccordion(plot);
			}
		}
	});
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
			console.log("success");
		}
	});
}


function createPlotAccordion(plot) {

	var num = plot._leaflet_id
	var name = plot.name ? plot.name : "Unnamed Plot"
	var description = plot.description ? plot.description : ""

	var newAccordion =  '<div id="plot-details-' + num + '" class="card" onclick="togglePlotFocus(' + num + ')">'
	newAccordion += '	<div class="card-header" id="heading-' + num + '">'
	newAccordion += '		<h2 class="mb-0">'
	newAccordion += '			<button id="plot-' + num + '-name" class="btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse-plot-' + num + '" aria-expanded="true" aria-controls="collapse-plot-' + num + '">' + name + '</button>'
    newAccordion += '		</h2>'
    newAccordion += '	</div>'
    newAccordion += '	<div id="collapse-plot-' + num + '" class="collapse" aria-labelledby="heading-plot-' + num + '" data-parent="#plots-accordion">'
    newAccordion += '	<div class="card-body">'
    newAccordion += '		<div class="card-body">'
    newAccordion += '			<div id="plot-' + num + ' description">'
    newAccordion += '				<p>' + description + '</p>'
	newAccordion += '			</div>'
	newAccordion += '		</div>'
	newAccordion += '	</div>'
	newAccordion += '</div>'

	$("#plots-accordion").append(newAccordion);
}

function updatePlotAccordion(plot) {

	$("#plot-" + plot._leaflet_id + "-name").val(plot.name);
	$("#plot-" + plot._leaflet_id + "-description").val(plot.description);
	$("#plot-" + plot._leaflet_id + "-description").val(plot.description);
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

		plotLayer._leaflet_id = plot.id;
		plotLayer.name = plot.name;
		plotLayer.addTo(map);

	  	featureGroup.addLayer(plotLayer);
		updatePolygonPopup(plotLayer, units);
	}
}

function updateAllPolygonAreas(map) {

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
  	var popUpMessage = "<b>" + name + "</b><br>" + convertedArea + ' ' + units.closest('label').text();

  	plot.bindPopup(popUpMessage);
}
