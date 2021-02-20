
function lineInsidePlot(A, B, plot) {

	var inPlot = true;
	if (A && B && plot) {
		var line = turf.lineString([[A.getLatLng().lat, A.getLatLng().lng], [B.getLatLng().lat, B.getLatLng().lng]]);
		var plot = turf.polygon(currentPlot.toGeoJSON().geometry.coordinates);
		inPlot = turf.lineIntersect(line, plot) == 0;
	}

	return inPlot;
}

function deletePlot(plot, successFunction, failureFunction) {
	deletePlots([plot], successFunction, failureFunction);
}

function deletePlots(plots, successFunction, failureFunction) {

	$.ajax({
		type: "POST",
		url: "ajax/delete-plots",
		dataType: "json",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			plots: JSON.stringify(plots)
		},
		success: function(data) {successFunction(data)},
		error: function(data) {failureFunction(data)}
	});
}
function persistPlot(plot, successFunction, failureFunction, returnPage) {

	$.ajax({
		type: "POST",
		url: "ajax/details",
		dataType: "html",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			id: plot._leaflet_id,
			name: plot.name,
			description: plot.description,
			area: plot.area,
			type: plot.type,
			parent: currentPlot._leaflet_id,
			points: JSON.stringify(plot.getLatLngs()),
			returnPage: returnPage
		},
		success: function(data) {successFunction(data)},
		error: function(data) {failureFunction(data)}
	});
}