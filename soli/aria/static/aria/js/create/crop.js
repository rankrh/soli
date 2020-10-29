var LAST_PAGE = 5;

function togglePattern() {

    var transplantDate = $("#transplant-date");
    if ($("input[name^='pl_location']:checked:visible").val() == "I") {
        transplantDate.show();
    } else {
        transplantDate.hide();
    }
}

function toggleSuccession() {

    var successionData = $("#succession-data");
    if ($("#succession").is(":checked")) {
        successionData.show();
    } else {
        successionData.hide();
    }
}

function previousPlantingScheme() {

	var currentPage = getCurrentPage();
	var previousPage = currentPage - 1;

	goToPage(previousPage);
}

function nextPlantingScheme() {

	var currentPage = getCurrentPage();
	var nextPage = currentPage + 1;

	goToPage(nextPage);
}

function getCurrentPage() {

	return parseInt($("div[id^='page-']:visible").prop('id').split('-')[1]);
}

function hideButtons(page) {

	var isFirstPage = page <= 1;
	var isLastPage = page >= LAST_PAGE;

	if (isLastPage) {
		$("#previousPlantingScheme").show();
		$("#nextPlantingScheme").hide();
		$("#submitPlantingScheme").show();
	} else if (isFirstPage) {
		$("#previousPlantingScheme").hide();
		$("#nextPlantingScheme").show();
		$("#submitPlantingScheme").hide();
	} else {
		$("#previousPlantingScheme").show();
		$("#nextPlantingScheme").show();
		$("#submitPlantingScheme").hide();
	}
}

function addPlantingScheme() {

	var plantingSchemes = $("#planting-schemes");

	createPlantingScheme();
	plantingSchemes.show();
}

function getPlantingSchemeJson() {

	var plantingScheme = {
		"schemeId": $("#planting-schemes-body").find("tr").length + 1,
		"variety": $("input[name='har_variety']:checked"),
		"location":$("input[name='pl_location']:checked"),
		"transplantWeeks": $("#transplant"),
		"sun": $("input[name='gr_sun']:checked"),
		"plantDate": $("input[name='pl_date']"),
		"isBefore": $("#beforeOrAfter").val() < 0,
		"frost": $("select[name='pl_frost'] option:selected"),
		"succession": $("#succession").prop("checked"),
		"successionPeriod": $("input[name=succession]"),
		"successionTime": $("input[name=times]"),
		"pattern": $("input[name=pl_pattern]:checked")
	};

	plantingScheme["plantDateFormatted"] = (plantingScheme.isBefore ? "-" : "+") + plantingScheme.plantDate.val();

	return plantingScheme;
}

function createPlantingScheme() {

	var plantingScheme = getPlantingSchemeJson();

	createPlantingSchemeRow(plantingScheme);
	storePlantingSchemeData(plantingScheme);
}

function storePlantingSchemeData(plantingScheme) {


}

function createPlantingSchemeRow(plantingScheme) {

	var plantingSchemesBody = $("#planting-schemes-body");

	row = "<tr id=\"planting-scheme-" + plantingScheme.schemeId + "\">";
	row += "<td>" + plantingScheme.variety.closest('label').text() + "<\/td>";
	row += "<td>" + plantingScheme.sun.closest('label').text() + "<\/td>";
	row += "<td>" + plantingScheme.location.closest('label').text() + "<\/td>";
	row += "<td>" + plantingScheme.frost.text() + plantingScheme.plantDateFormatted + "<\/td>";
	row += "<td>" + (plantingScheme.succession ? "Every " + plantingScheme.successionPeriod.closest('label').text() + " weeks for " + plantingScheme.successionTime.val() + " weeks." : "") + "<\/td>";
	row += "<td>" + plantingScheme.pattern.closest('label').text() + "<\/td>";
	row += "<td><div class=\"btn-group\">";
	row += "<button type=\"button\" class=\"btn btn-secondary\" onchange=\"editPlantingScheme(" + plantingScheme.schemeId + ")\">Edit<\/button>";
	row += "<button type=\"button\" class=\"btn btn-secondary\" onchante=\"deletePlantingScheme(" + plantingScheme.schemeId + "\">Delete<\/button>";
	row += "<\/div><\/td>"
	row += "<\/tr>";

	plantingSchemesBody.append(row);
}

function goToPage(page) {

	$("div[id^=page-]").hide();
	$("#page-" + page).show()
	hideButtons(page);
}