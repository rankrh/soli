function createGenus() {

	$.ajax({
		url: 'ajax/genus',
		type: "POST",
		dataType: 'json',
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			ge_name: $("input[name='ge_name']").val()
		},
		dataType: 'json',
		success: function (data) {
			createGenusSuccess(data);
		}
	})
}

function createGenusSuccess(genus) {

	if (genus.errors.length) {
		var errorBar = $("#addGenusModal-errors");
		for (error in genus.errors) {
		console.log(error);
			errorBar.html("<span>" + genus.errors + "</span");
		}
		errorBar.show();
	} else {
		$("input[name='ge_name']").val("");
		console.log(genus);
		$('#id_ge_num').append(new Option(genus.ge_name, genus.ge_num));
		$("#createGenus").modal('hide');
		$("#id_ge_num").val(genus.ge_num);
	}
}

