map.on(L.Draw.Event.CREATED, function(e) {
	var plot = e.layer;
	plot.setStyle({fillColor: plotColors.unknown.fill, fillOpacity:0.5, color:plotColors.unknown.outline})
	updatePolygonArea(plot);
	persistSubplot(plot);
});

map.on(L.Draw.Event.EDITED, function (e) {
	e.layers.eachLayer(function(layer) {
		persistSubplot(layer);
	});
	updatePlotAreas(subdivisions, "acres");
});

map.on("click", function (e) {
	unselectAllSubplots();
});

map.on('draw:deleted', function (e) {

	var plotsToDelete = []

	e.layers.eachLayer(function(layer) {
		plotsToDelete.push(layer._leaflet_id)
	});

	deletePlots(
		plotsToDelete,
		successFunction = function(data) {
			for (var i = 0; i < plotsToDelete.length; i++) {
				deleteSubPlotAccordion(plotsToDelete[i]);
			}

			if (!subdivisions.getLayers().length) {
				$("#no-plots-header").show();
			}
		}
	);
});

$(initializePlots());

function deleteSubPlotAccordion(plot) {

	$("#subplot-" + plot).remove();
}

function saveSubplotDetails() {

	var plot = subdivisions.getLayer(Number($("#edit-plot-id").val()));
	var subplotDetails = $("#subplot-" + plot._leaflet_id);

	plot.name = $("#edit-plot-name").val();
	plot.description = $("#edit-plot-description").val();
	plot.type = $("#edit-plot-type").val();

	persistSubplot(plot);
	updatePolygonArea(plot);
	updatePolygonPopup(plot, $("input[type=radio][name=units]:checked").text());
	updatePolygonColor(plot, plotColors[plot.type].fill, plotVisibility.child, plotColors[plot.type].outline);
	clearEditPlotModal();

	$("#subplot-" + plot._leaflet_id + "-name").text(plot.name);

}

function updateUIAfterSave(plot) {

	updatePlotAccordion(plot);
	updatePolygonArea(plot);
	updatePolygonPopup(plot, $("input[type=radio][name=units]:checked"))
	clearEditPlotModal();
}

function clearEditPlotModal() {

	$("#edit-plot-modal").modal("toggle");
	$("#edit-plot-name").val("");
	$("#edit-plot-description").val("");
}

var curPt = null;

var drawControl = new L.Control.Draw({
  	edit: {
  		featureGroup: subdivisions,
  	},
  	draw: {
    	polygon: {
            icon: new L.DivIcon({
			  iconSize: [8, 8],
			  className: 'leaflet-div-icon leaflet-drawing-icon',
			}),
            shapeOptions: {
                color: '#FF0000',
                opacity: 1,
                weight: 2
            }
        },
    	polyline: true,
    	rectangle: false,
    	circle: false,
    	marker: true,
  	}
})
.addTo(map);

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


function initializePlots() {

	addSavedPlots(plotJSON);
	var units = $("input[type=radio][name=units]:checked").val();

	updatePlotAreas(basePlots, units);
	updatePlotAreas(subdivisions, units);
	var firstPlot = basePlots.getLayer(plotJSON[0].id);

	if (firstPlot) {
		map.fitBounds(firstPlot.getBounds());
		firstPlot.getPopup().openPopup();
		currentPlot = firstPlot;
		currentPlotIndex = 0;
	}
}

function persistSubplot(plot) {

	persistPlot(plot,
		successFunction=function(data) {
			var plotHTML = $(data);
			var plotId = plotHTML.attr("data-id");
			if (plot._leaflet_id != plotId) {
				$("#no-plots-header").hide();
				plot._leaflet_id = plotId;
				subdivisions.addLayer(plot);
				$("#plot-" + currentPlot._leaflet_id + "-subplots").append(plotHTML);
				editPlotDetails(plot);
			} else {
			}
		},
		errorFunction=function(data) {},
		returnPage="aria/create/subplotDetails"
	);
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

function updatePlotAccordion(plot) {

	$("#plot-" + plot._leaflet_id + "-name").text(plot.name);
	$("#plot-" + plot._leaflet_id + "-description").text(plot.description);
}

function nextPlot() {

	currentPlotIndex = currentPlotIndex + 1 < basePlots.getLayers().length ? currentPlotIndex + 1 : 0;
	focusCurrentPlot();
}

function previousPlot() {

	currentPlotIndex = currentPlotIndex - 1 >= 0 ? currentPlotIndex - 1 : basePlots.getLayers().length - 1;
	focusCurrentPlot();
}

function focusCurrentPlot() {

	currentPlot = basePlots.getLayers()[currentPlotIndex];
	map.fitBounds(currentPlot.getBounds());
	$("div[id^='plot-overview-']").hide();
	$("#plot-overview-" + currentPlot._leaflet_id).show();
}
