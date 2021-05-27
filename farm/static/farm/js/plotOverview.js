var farmId = JSON.parse($("#farm-id").text());
var coordinates = JSON.parse($("#farm-location").text());
var plotJSON = JSON.parse($("#plots-data").text());
var plotDetailsModal = $("#edit-plot-modal");

var map = initializeMap("map", coordinates, 15, false);
var basePlots = L.featureGroup().addTo(map);
var subdivisions = L.featureGroup().addTo(map);

var drawControl = new L.Control.Draw({
  	edit: { featureGroup: basePlots },
  	draw: {
    	polygon: true,
    	polyline: false,
    	rectangle: false,
    	circle: false,
    	marker: false
  	}
}).addTo(map);

map.on('draw:created', function (e) {
	createPlot(e.layer)
});

map.on('draw:edited', function (e) {
	e.layers.eachLayer(function(plot) {
		persistPlot(plot);
	});
	updatePlotAreas();
});

map.on('draw:deleted', function (e) {

	let plotsToDelete = [];

	e.layers.eachLayer(function(layer) {
		plotsToDelete.push(layer.id)
	});
	deletePlots(plotsToDelete);
});

$(initializePlots());

function initializePlots() {
	addSavedPlots();
	zoomToBounds(basePlots);
	updatePlotAreas();
}

function updatePlotAreas() {
 	basePlots.eachLayer(function(layer) {
 		updatePolygonArea(layer);
 		updatePolygonPopup(layer);
 	});
}

function updatePolygonArea(plot) {

	plot.area = LGeo.area(plot);
}

function updatePolygonPopup(plot, units) {

	var convertedArea = Math.round(plot.area * 100) / 100;
	var name = plot.name ? plot.name : "Unnamed Plot"
	unitName = "square meters";

  	var popUpMessage = "<div id=\"popup-" + plot.id + "\">";
  	popUpMessage += "<b>" + name + "</b><br>";
  	if (plot.type && plot.type != "unknown") {
  		popUpMessage += "(" + plotColors[plot.type].name + ")<br>"
  	}
  	popUpMessage += convertedArea + ' ' + unitName;
  	popUpMessage += "</div>";

  	plot.bindPopup(popUpMessage);
}

function addSavedPlots() {
	for (i=0; i < plotJSON.length; i++) {
		var plotData = plotJSON[i];
		var plot = setPlotInformation(plotData);

		plot.setStyle({fillOpacity: plotVisibility.parent});
		basePlots.addLayer(plot);
		if (plotData.children) {
			addSavedChildPlots(plotData.children);
		}

		plot.addTo(map);
	}
}

function setPlotInformation(plotData) {

	var plot = L.polygon([plotData.points]);
	plot._leaflet_id = plotData.id;
	plot.id= plotData.id;
	plot.name = plotData.name;
	plot.parent = plotData.parent;
	plot.type = plotData.type ? plotData.type : "unknown";

	return plot;
}

function createPlot(plot) {
	findPlotArea(plot);
	persistPlot(plot);
}

function findPlotArea(plot) {
	plot.area = LGeo.area(plot);
}

function deletePlots(plots) {

	$.ajax({
		type: "POST",
		url: "plots/delete",
		dataType: "json",
		data : {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			farm: farmId,
			plots: JSON.stringify(plots)
		}
	});
}

function persistPlot(plot) {
	$.ajax({
		type: "POST",
		url: "plots/create",
		dataType: "html",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			farm: farmId,
			plot: plot.id,
			name: plot.name,
			description: plot.description,
			area: plot.area,
			points: JSON.stringify(plot.getLatLngs())
		},
		success: function(data) {
			var details = $(data);
			var plotId = details.find("div[id^='plot-id-']").data("plot-id");

			if (!basePlots.getLayers().includes(plot)) {
				var plotSidebar = $("#plots-sidebar");

				$("#no-plot-data").hide();
				plotSidebar.append(data);
				plot._leaflet_id = plotId;
				plot.id = plotId;
				basePlots.addLayer(plot);
				setModalPlot(plotId);
				plotDetailsModal.modal("toggle");
			}
		}
	});
}

function getModalPlot() {
    return plotDetailsModal.data("plot-id")
}

function setModalPlot(id) {
    plotDetailsModal.data("plot-id", id);
}

function zoomToBounds(boundedLayer) {

	if (boundedLayer && boundedLayer.getLayers().length) {
		map.fitBounds(boundedLayer.getBounds());
	}
}

function savePlotDetails() {

    let plot = basePlots.getLayer(getModalPlot());
    plot.name = $("#edit-plot-name").val();
    plot.description = $("#edit-plot-description").val();
    persistPlot(plot);
    plotDetailsModal.modal("hide");
    setModalPlot("");
}
