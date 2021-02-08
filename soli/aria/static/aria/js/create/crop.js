function updateLocation(locationData) {

	var num = Number(locationData.name.split("-")[1]);
	var transplantDate = $("#transplant-" + num);

	if ($("select[name^='planting_set-" + num + "-location']").val() == "I") {
		transplantDate.show();
	} else {
		transplantDate.hide();
	}
}

function addPlanting() {

	var nextPlantingNum = $("#id_planting_set-TOTAL_FORMS").val();

	
}

$("select[name^='planting_set'][name$='location']").change(function() { updateLocation(this) });