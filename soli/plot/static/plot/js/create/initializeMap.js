L.mapbox.accessToken = 'pk.eyJ1IjoicmFua3JoIiwiYSI6ImNraDFnbjlrcTAxZjMydG4xN2dyNmtoYWUifQ.tlJBm2GyxVZapHdK0_oDyQ';

const plotJSON = JSON.parse($("#plots-data").text());

var map = L.mapbox.map('map')
    .setView([40, -100], 4)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/rankrh/ckhcwof2w17fa19o2uo8pmzdr'))
    .addControl(L.mapbox.geocoderControl('mapbox.places'));

L.Draw.Polygon = L.Draw.Polygon.extend({
  options: {
    icon: new L.DivIcon({
      iconSize: [8, 8],
      className: 'leaflet-div-icon leaflet-drawing-icon',
    }),
  }
});

L.Edit.Poly = L.Edit.Poly.extend({
  options: {
    icon: new L.DivIcon({
      iconSize: [8, 8],
      className: 'leaflet-div-icon leaflet-editing-icon',
    }),
  },
});

var basePlots = L.featureGroup().addTo(map);
var subdivisions = L.featureGroup().addTo(map);
var currentPlot = null;
var currentPlotIndex = null;

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
			fillOpacity: plotVisibility.child,
			color:plotColors[childPlot.type].outline
		});

		childPlot.on("click", function(e) {
			zoomToSubPlot(e.target._leaflet_id);
		})

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
}

function zoomToSubPlot(plotId) {

	var plot = subdivisions.getLayer(plotId);
	var plotBtn = $("#subplot-" + plotId);

	map.fitBounds(plot.getBounds());
	plot.openPopup();
	unselectAllSubplots();
	plotBtn.addClass("active");
}

function unselectAllSubplots() {
	$("button[id^='subplot-']").removeClass("active");
}