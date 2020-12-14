var subdivisions = L.featureGroup().addTo(map);
var currentPlot = null;
var curPt = null;

var drawControl = new L.Control.Draw({
  	edit: {
  		featureGroup: subdivisions,
  	},
  	draw: {
    	polygon: true,
    	polyline: true,
    	rectangle: false,
    	circle: false,
    	marker: true,
  	}
}).addTo(map);

/*map.on(L.Draw.Event.DRAWVERTEX , function(e) {
	var layers = e.layers.getLayers();
	var created = layers[layers.length - 1];
	var legalPoint = true;

	if (layers.length < 2) {
		legalPoint = turf.booleanPointInPolygon(created.toGeoJSON(), currentPlot.toGeoJSON());
	} else {
		var lastVertex = layers[layers.length - 2];
		legalPoint = lineInsidePlot(created, lastVertex, currentPlot);
	}

	if (!legalPoint) {
		console.log("ILLEGAL");
	}
});*/

map.on(L.Draw.Event.CREATED, function(e) {

	var plot = e.layer;
	plot.setStyle({fillColor: '#11a033', fillOpacity:0.5, color:"#074215"})
	updatePolygonArea(plot);
	persistSubplot(plot);
	editPlotDetails(plot);
});

map.on(L.Draw.Event.EDITED, function (e) {
	e.layers.eachLayer(function(layer) {
		persistSubplot(layer);
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

function persistSubplot(plot) {

	$.ajax({
		type: "POST",
		url: "ajax/details",
		dataType: "json",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			id: plot._leaflet_id,
			name: plot.name,
			description: plot.description,
			area: plot.area,
			type: plot.type,
			parent: currentPlot._leaflet_id,
			points: JSON.stringify(plot.getLatLngs())
		},
		success: function(data) {
			$("#edit-plot-id").val(data.plot);
			plot._leaflet_id = data.plot;
			subdivisions.addLayer(plot);

			if ($("#plot-details-" + plot._leaflet_id).length == 0) {
				//createPlotAccordion(plot);
			}
		}
	});
}

function initializePlots() {

	addSavedPlots();
	updateAllPolygonAreas();
	var firstPlot = basePlots.getLayers()[0];

	if (firstPlot) {
		zoomToBounds(firstPlot);
		firstPlot.getPopup().openPopup();
		currentPlot = firstPlot;
	}
}


function editPlotDetails(plot) {

	$("#edit-plot-id").val(plot._leaflet_id);

	if (plot.name) {
		$("#edit-plot-name").val(plot.name)
	}

	if (plot.description) {
		$("#edit-plot-description").val(plot.description)
	}

	$("#edit-plot-modal").modal("toggle");
}

function saveSubplotDetails() {

	var plot = basePlots.getLayer(Number($("#edit-plot-id").val()));

	plot.name = $("#edit-plot-name").val();
	plot.description = $("#edit-plot-description").val();

	persistSubplot(plot);
	updatePlotAccordion(plot);
	updatePolygonArea(plot);
	updatePolygonPopup(plot, $("input[type=radio][name=units]:checked"))
	clearEditPlotModal();
}

function updatePlotAccordion(plot) {

	$("#plot-" + plot._leaflet_id + "-name").text(plot.name);
	$("#plot-" + plot._leaflet_id + "-description").text(plot.description);
}