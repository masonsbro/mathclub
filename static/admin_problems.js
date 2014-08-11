$(function() {
	$("#skill").change(function(event) {
		var curValue = parseInt($("#learn_item option:selected").val());
		$("#learn_item optgroup").remove();
		$("#learn_item").empty();
		$.getJSON("/ajax/learn_items/skill/" + $("#skill").val() + "/", function(data) {
			$("#learn_item").empty();
			data.forEach(function(element) {
				if (curValue == element.pk) {
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
