function createGenus() {

    $.ajax({
        url: 'ajax/species',
        type: "POST",
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            genus: $("input[name='genus']").val()
        },
        dataType: 'json',
        success: function (data) {
            createGenusSuccess(data);
         }
    })
}

function createGenusSuccess(data) {

    if (data.errors.length) {
        var errorBar = $("#addGenusModal-errors");
        for (error in data.errors) {
        console.log(error);
            errorBar.html("<span>" + data.errors + "</span");
        }
        errorBar.show();
    } else {
        $("input[name='genus']").val("");
        $('#id_genus').append(new Option(data.genus, data.id));
        $("#createGenus").modal('hide');
    }
}

