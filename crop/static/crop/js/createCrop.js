function updateLocation() {

	$("select[name^='plantingdate_set-'][name$='location']").each(
		function() {
			var locationData = $(this);
			var num = Number(locationData.attr("name").split("-")[1]);
			var transplantDate = $("#id_plantingdate_set-" + num + "-transplant");

			if (locationData.val() == "I") {
				transplantDate.show();
			} else {
				transplantDate.hide();
			}
		}
	);

}

function addPlanting() {

	var newPlantingDates = updateElementIndex(
		$("#id_plantingdate_set-0-dates").clone(true),
		"plantingdate_set-",
		$("#id_plantingdate_set-TOTAL_FORMS").val()
	);

	updateManagementForm("plantingdate_set-");
	$("#all-planting-dates").append(newPlantingDates);
	updateLocation();
}

function updateElementIndex(element, prefix, index) {

	return $(element.get(0).outerHTML.replace(
		RegExp(prefix + `(\\d{1})`, 'g'),
		prefix + index)
	)
}

function updateManagementForm(prefix) {

	var managementForm = $("#id_"+ prefix + "TOTAL_FORMS");
	managementForm.val(Number(managementForm.val()) + 1);
}
