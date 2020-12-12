var drawControl = new L.Control.Draw({
  	edit: {
  		featureGroup: featureGroup,
  	},

  	draw: {
    	polygon: true,
    	polyline: true,
    	rectangle: true,
    	circle: true,
    	marker: true
  	}
}).addTo(map);

$(initializePlots());

function initializePlots() {

	addSavedPlots();
	updateAllPolygonAreas();
	var firstPlot = featureGroup.getLayers()[0];

	if (firstPlot) {
		zoomToBounds(firstPlot);
		firstPlot.getPopup().openPopup();
	}
}