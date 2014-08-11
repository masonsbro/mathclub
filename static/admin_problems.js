$(function() {
	$("#skill").change(function(event) {
		var values = $.map($('#learn_item option:selected'), function(e) { return parseInt(e.value); });
		console.log(values);
		$("#learn_item optgroup").remove();
		$("#learn_item").empty();
		$.getJSON("/ajax/learn_items/skill/" + $("#skill").val() + "/", function(data) {
			$("#learn_item").empty();
			data.forEach(function(element) {
				console.log(element.pk);
				console.log($.inArray(element.pk, values));
				if ($.inArray(element.pk, values) != -1) {
					$("#learn_item").append("<option value=\"" + element.pk + "\" selected>" + element.fields.title + "</option>");
				} else {
					$("#learn_item").append("<option value=\"" + element.pk + "\">" + element.fields.title + "</option>");
				}
			});
		});
	});
	// update as soon as page loads if already selected (i.e. editing)
	if ($("#skill").val() != "-1") {
		$("#skill").change();
	}
});
