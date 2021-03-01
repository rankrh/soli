function updatePlotAreas(plots, units) {

	plots.eachLayer(function(layer) {
 		updatePolygonArea(layer);
 		updatePolygonPopup(layer, units);
	});
}

function updatePolygonArea(plot) {

	plot.area = LGeo.area(plot);
}

function updatePolygonPopup(plot, units) {

	units = units ? units : "acres";
	var convertedArea = convertArea(plot.area, units);
	var name = plot.name ? plot.name : "Unnamed Plot"

  	var popUpMessage = "<div id=\"popup-" + plot._leaflet_id + "\">";
  	popUpMessage += "<b>" + name + "</b><br>";
  	if (plot.type && plot.type != "unknown") {
  		popUpMessage += "(" + plotColors[plot.type].name + ")<br>"
  	}
  	popUpMessage += convertedArea + ' ' + units;
  	popUpMessage += "</div>";

  	plot.bindPopup(popUpMessage);
}

function updatePolygonColor(polygon, fill, opacity, outline) {

	polygon.setStyle({
		fillColor: fill,
		fillOpacity: opacity,
		color: outline
	});
}
