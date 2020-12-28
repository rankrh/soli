let farm = JSON.parse($("#farm-data").text())

L.UnitsControl = L.Control.extend({
  options: {
    position: 'topleft'
  },
  initialize: function(options) {
    L.Util.setOptions(this, options);
  },
  onAdd: function(map) {
    var controlElementTag = 'div';
    var controlElementClass = 'units-control';
    var controlElement = L.DomUtil.create(controlElementTag, controlElementClass);
    return controlElement;
  },
  onRemove: function(map) {
  },

});

var unitsControl = new L.UnitsControl().addTo(map);

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
	var plot = e.layer;

	updatePolygonArea(plot);
	persistPlot(plot);
	editPlotDetails(plot);
});

map.on('draw:edited', function (e) {
	e.layers.eachLayer(function(layer) {
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

	if (farm) {
		addSavedPlots(plotJSON);
		zoomToBounds(basePlots);
		updateAllPolygonAreas();
	} else {
		$.ajax({
			type: "GET",
			url: "farm",
			dataType: "html",

			success: function(data) {
				$("#create-farm-modal-body").html(data);
				$("#create-farm-modal").modal('toggle');
			},
		});
	}
}

function createFarmSidebar() {

	$("#farm").text($("#farm-name").val());
	$("#farm-details").show();
	$("#no-farm-data-block").hide();
}

function saveFarm() {

	var spinner = $("#farm-spinner");
	var modalBody = $("#farm-modal-content");

	$.ajax({
		type: "POST",
		url: "farm",
		dataType: "json",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			name: $("#farm-name").val(),
			logo: $("#farm-logo").val()
		},
		success: function(data) {
			$("#create-farm-modal").modal('toggle');
			farmId = data.id;
			createFarmSidebar();
		},
		error: function(data) {
			$("#farm-modal-content").show();
			$("#farm-spinner").hide();
		}
	});

	modalBody.hide();
	spinner.show();
}

function expandPlotDetails(plotId) {

	togglePlotFocus(plotId);
	$("#plot-" + plotId + "-tools").toggle();
}

function togglePlotFocus(plotId) {

	var boundedLayer = basePlots;
	if (!$("#collapse-plot-" + plotId).hasClass("show")) {
		boundedLayer = basePlots.getLayer(plotId);
		boundedLayer.openPopup();
	}

	zoomToBounds(boundedLayer);
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
			basePlots.addLayer(plot);

			if ($("#plot-details-" + plot._leaflet_id).length == 0) {
				createPlotAccordion(plot);
			}
		}
	});
}

function createPlotAccordion(plot) {

	var num = plot._leaflet_id
	var name = plot.name ? plot.name : "Unnamed Plot"
	var description = plot.description ? plot.description : ""

	var newAccordion = '<div id="plot-details-' + num + '" class="list-group-item" onclick="togglePlotFocus(' + num + ')">'
	newAccordion += '	<h3><div id="plot-' + num + '-name" class="plot-header text-left" id="heading-' + num + '" data-toggle="collapse" data-target="#collapse-plot-' + num + '" aria-expanded="true" aria-controls="collapse-plot-' + num + '">'
	newAccordion += name
	newAccordion += '	</div></h3>'
	newAccordion += '	<div id="collapse-plot-' + num + '" class="collapse" aria-labelledby="heading-plot-' + num + '" data-parent="#plots-accordion">'
	newAccordion += '		<div class="card-body">'
	newAccordion += '			<button class="btn btn-sm btn-light justify-content-center align-self-center" onclick="editPlotDetails(basePlots.getLayer(' + num + '))">'
	newAccordion += '				<svg viewBox="0 0 8 8" class="icon">'
	newAccordion += '					<use xlink:href="#pencil"></use>'
	newAccordion += '				</svg>'
	newAccordion += '			</button>'
	newAccordion += '		<div id="plot-' + num + '-description">'
	newAccordion += '			<p>' + description + '</p>'
	newAccordion += '		</div>'
	newAccordion += '	</div>'
	newAccordion += '</div>'


	$("#plots-accordion").append(newAccordion);
}

function updatePlotAccordion(plot) {

	$("#plot-" + plot._leaflet_id + "-name").text(plot.name);
	$("#plot-" + plot._leaflet_id + "-description").text(plot.description);
}

function deletePlotAccordion(plotId) {

	$("#plot-details-" + plotId).remove();
}

function zoomToBounds(boundedLayer) {

	if (boundedLayer && boundedLayer.getLayers().length) {
		map.fitBounds(boundedLayer.getBounds());
	}
}
