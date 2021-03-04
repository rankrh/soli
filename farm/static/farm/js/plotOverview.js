let coordinates = JSON.parse($("#farm-location").text())
var map = initializeMap("map", coordinates, 15, false)

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