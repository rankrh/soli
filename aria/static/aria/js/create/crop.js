function togglePattern() {

    var transplantDate = $("#transplant-date");
    if ($("input[name='plant_set-0-location']:checked").val() == "I") {
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