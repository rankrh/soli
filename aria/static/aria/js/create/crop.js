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

function goToPage(page) {

	$("div[id^=page-]").hide();
	$("#page-" + page).show()
	hideButtons(page);
}