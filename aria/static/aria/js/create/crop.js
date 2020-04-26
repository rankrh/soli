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