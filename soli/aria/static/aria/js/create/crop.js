var LAST_PAGE = 5;

function togglePattern() {

    var transplantDate = $("#transplant-date");
    if ($("input[name^='location']:checked:visible").val() == "I") {
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
	var plantingSchemesBody = $("#planting-schemes-body");

	plantingSchemesBody.append(createPlantingSchemeRow());
	plantingSchemes.show();
}

function createPlantingSchemeRow() {

	var variety = $("input[name='variety']:checked").val();
	var location = $("input[name='location']:checked").val();
	var transplantWeeks = location == "I" ? $("#transplant").val() : null;
	var sun = $("input[name='sun']:checked").val();
	var plantDate = $("input[name='date']").val() * $("#beforeOrAfter").val();
	var frost = $("select[name='frost']").val();
	var succession = $("#succession").is("checked");
	var successionPeriod = succession ? $("input[name=succession]").val() : null;
	var successionTime = succession ? $("input[name=times]").val() : null;
	var pattern = $("input[name=pattern]:checked").val();

	return "<tr><td>" + variety + "</td></tr>"
}

function goToPage(page) {

	$("div[id^=page-]").hide();
	$("#page-" + page).show()
	hideButtons(page);
}