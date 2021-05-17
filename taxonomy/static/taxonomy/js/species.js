function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function createGenus() {

	$.ajax({
		type: "POST",
		url: "/admin/crop/genus/create",
		dataType: "json",
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			name: $("#genus_name").val(),
		},
		success: function(data) {
		    createGenusSuccess(data);
		}
	});
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
