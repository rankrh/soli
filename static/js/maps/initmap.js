L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

function initializeMap(container, coordinates, zoom, search) {

	var map = L.mapbox.map(container)
    .setView(coordinates, zoom)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'));

    if (search) {
    	map.addControl(L.mapbox.geocoderControl('mapbox.places'));
    }

	return map;
}



//const plotJSON = JSON.parse($("#plots-data").text());

/*

var basePlots = L.featureGroup().addTo(map);
var subdivisions = L.featureGroup().addTo(map);

function setPlotInformation(plotData) {

	var plot = L.polygon([plotData.points]);
	plot._leaflet_id = plotData.id;
	plot.name = plotData.name;
	plot.parent = plotData.parent;
	plot.type = plotData.type ? plotData.type : "unknown";

	return plot;
}

function addSavedChildPlots(childPlots) {

	for (j=0; j<childPlots.length; j++) {
		var childPlotData = childPlots[j];
		var childPlot = setPlotInformation(childPlotData);

		childPlot.setStyle({
			fillColor: plotColors[childPlot.type].fill,
			fillOpacity:plotVisibility.child,
			color:plotColors[childPlot.type].outline
		});

		subdivisions.addLayer(childPlot);
	}
}

function addSavedPlots(plots) {

	for (i=0; i < plots.length; i++) {
		var plotData = plots[i];
		var plot = setPlotInformation(plotData);

		plot.setStyle({fillOpacity: plotVisibility.parent});
		basePlots.addLayer(plot);
		if (plotData.children) {
			addSavedChildPlots(plotData.children);
		}

		plot.addTo(map);
	}

	subdivisions.eachLayer(function(layer) {
		layer.on("click", function(e) {
			zoomToSubPlot(e.target._leaflet_id);
		});
	});
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

  	var popUpMessage = "<div id=\"popup-" + plot._leaflet_id + "\">";
  	popUpMessage += "<b>" + name + "</b><br>";
  	if (plot.type && plot.type != "unknown") {
  		popUpMessage += "(" + plotColors[plot.type].name + ")<br>"
  	}
  	popUpMessage += convertedArea + ' ' + unitName;
  	popUpMessage += "</div>";

  	plot.bindPopup(popUpMessage);
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

function saveSubplotDetails() {

	var plot = subdivisions.getLayer(Number($("#edit-plot-id").val()));
	var subplotDetails = $("#subplot-" + plot._leaflet_id);

	plot.name = $("#edit-plot-name").val();
	plot.description = $("#edit-plot-description").val();
	plot.type = $("#edit-plot-type").val();

	persistSubplot(plot);
	updatePolygonArea(plot);
	updatePolygonPopup(plot, $("input[type=radio][name=units]:checked"))
	clearEditPlotModal();

	if (subplotDetails.length) {
		$("#subplot-" + plot._leaflet_id).text(plot.name);
	} else {
		var div = "<div id=\"subplot-" + plot._leaflet_id + "\" type=\"button\" class=\"list-group-item list-group-item-action\" onclick=\"zoomToSubPlot(" + plot._leaflet_id + ")\">";
		div += plot.name;
		div += "</div>";
		$("#plot-" + currentPlot._leaflet_id + "-subplots").append(div);
	}
}


function savePlotDetails() {

	var plot = basePlots.getLayer(Number($("#edit-plot-id").val()));
	plot.name = $("#edit-plot-name").val();
	plot.description = $("#edit-plot-description").val();

	persistPlot(plot);
	updateUIAfterSave(plot);
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
}*/
